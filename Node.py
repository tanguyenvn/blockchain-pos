import copy

from Block import Block
from Blockchain import Blockchain
from Message import Message
from NodeAPI import NodeAPI
from SocketCommunication import SocketCommunication
from TransactionPool import TransactionPool
from Utils import Utils
from Wallet import Wallet


class Node:
    def __init__(self, ip, port, keyFile=None):
        self.p2p = None
        self.ip = ip
        self.port = port

        self.transactionPool = TransactionPool()
        self.blockchain = Blockchain()
        self.wallet = Wallet()  # to sign block
        if keyFile is not None:
            self.wallet.fromKey(keyFile)

    # Start a P2P node
    def startP2P(self):
        self.p2p = SocketCommunication(self.ip, self.port)
        self.p2p.startSocketCommunication(self)

    # Start a webserver
    def startAPI(self, apiPort):
        self.api = NodeAPI()
        self.api.start(apiPort, self)

    # Handle transaction request
    def handleTransaction(self, transaction):
        data = transaction.getPayload()
        signature = transaction.signature
        signerPubKey = transaction.senderPubKey
        isSignatureValid = Wallet.isSignatureValid(data, signature, signerPubKey)
        transactionExistsInPool = self.transactionPool.transactionExists(transaction)
        transactionExistsInBlockchain = self.blockchain.transactionExists(transaction)

        if not transactionExistsInPool and not transactionExistsInBlockchain and isSignatureValid:
            self.transactionPool.addTransaction(transaction)
            message = Message(self.p2p.socketConnector, 'TRANSACTION', transaction)
            encodedMessage = Utils.encode(message)
            self.p2p.broadcast(encodedMessage)

            if self.transactionPool.isForgerRequired():
                self.forge()

    # Handle block message sent from other peers
    def handleBlock(self, block: Block):
        isBlockCountValid = self.blockchain.blockCountValid(block)
        isLastBlockHashValid = self.blockchain.lastBlockHashValid(block)
        isForgerValid = self.blockchain.forgerValid(block)
        areTransactionsValid = self.blockchain.transactionsValid(block.transactions)

        forger = block.forger
        signature = block.signature
        isSignatureValid = self.wallet.isSignatureValid(block.payload(), signature, forger)

        if not isBlockCountValid:
            self.requestChain()

        if isBlockCountValid and isLastBlockHashValid and isForgerValid and areTransactionsValid and isSignatureValid:
            # add to blockchain
            self.blockchain.addBlock(block)
            self.transactionPool.removeFromPool(block.transactions)

            # broadcast to other peers
            message = Message(self.p2p.socketConnector, 'BLOCK', block)
            self.p2p.broadcast(Utils.encode(message))

    # Request missing blocks sent from other peers
    def requestChain(self):
        message = Message(self.p2p.socketConnector, 'BLOCKCHAINREQUEST', None)
        self.p2p.broadcast(Utils.encode(message))

    # Handle blockchain request message sent from other peers
    def handleBlockchainRequest(self, requestingNode):
        message = Message(self.p2p.socketConnector, 'BLOCKCHAIN', self.blockchain)
        self.p2p.send(requestingNode, Utils.encode(message))
    
    # Handle blockchain message sent from other peers
    def handleBlockchain(self, blockchain):
        localBlockchainCopy = copy.deepcopy(self.blockchain)
        localBlockCount = len(localBlockchainCopy.blocks)
        receivedBlockCount = len(blockchain.blocks)
        if localBlockCount < receivedBlockCount:
            for blockNumber, block in enumerate(blockchain.blocks):
                if blockNumber >= localBlockCount:
                    localBlockchainCopy.addBlock(block)
                    self.transactionPool.removeFromPool(block.transactions)
            self.blockchain = localBlockchainCopy

    # Create a new block (PoS uses the terms forge, mint while PoW use the term mine)
    def forge(self):
        forger = self.blockchain.findNextForger()
        if forger == self.wallet.getPubKeyString():
            print('I am the next forger')
            # forge a block
            block = self.blockchain.createBlock(self.transactionPool.transactions, self.wallet)
            self.transactionPool.removeFromPool(block.transactions)
            
            # broadcast
            message = Message(self.p2p.socketConnector, 'BLOCK', block)
            self.p2p.broadcast(Utils.encode(message))
        else:
            print('I am not the next forger')
