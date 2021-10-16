from Blockchain import Blockchain
from SocketCommunication import SocketCommunication
from TransactionPool import TransactionPool
from Wallet import Wallet
from NodeAPI import NodeAPI


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
        self.p2p.startSocketCommunication()

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