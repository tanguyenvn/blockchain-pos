from Blockchain import Blockchain
from SocketCommunication import SocketCommunication
from TransactionPool import TransactionPool
from Wallet import Wallet


class Node:
    def __init__(self, ip, port):
        self.p2p = None
        self.ip = ip
        self.port = port

        self.transactionPool = TransactionPool()
        self.wallet = Wallet()  # to sign block
        self.blockchain = Blockchain()

    def startP2P(self):
        self.p2p = SocketCommunication(self.ip, self.port)
        self.p2p.startSocketCommunication()
