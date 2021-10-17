from Blockchain import Blockchain
from Message import Message
from NodeAPI import NodeAPI
from SocketCommunication import SocketCommunication
from TransactionPool import TransactionPool
from Utils import Utils
from Wallet import Wallet


class Node:
    def __init__(self, ip, port):
        self.p2p = None
        self.ip = ip
        self.port = port

        self.transactionPool = TransactionPool()
        self.wallet = Wallet()  # to sign block
        self.blockchain = Blockchain()

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
        transactionExists = self.transactionPool.transactionExists(transaction)
        if not transactionExists and isSignatureValid:
            self.transactionPool.addTransaction(transaction)
            message = Message(self.p2p.socketConnector, 'TRANSACTION', transaction)
            encodedMessage = Utils.encode(message)
            self.p2p.broadcast(encodedMessage)

            if self.transactionPool.isForgerRequired():
                self.forge()

    # create a new block (PoS uses the terms forge, mint while PoW use the term mine)
    def forge(self):
        forger = self.blockchain.nextForger()
        if forger == self.wallet.getPubKeyString():
            print('I am the next forger')
        else:
            print('I am not the next forger')
