import json
from p2pnetwork.node import Node

from PeerDiscoveryHandler import PeerDiscoveryHandler
from SocketConnector import SocketConnector
from Utils import Utils


# extends p2pnetwork.Node
class SocketCommunication(Node):
    def __init__(self, ip, port):
        super(SocketCommunication, self).__init__(ip, port, None)
        self.peers = []
        self.peerDiscoveryHandler = PeerDiscoveryHandler(self)
        self.socketConnector = SocketConnector(ip, port)

    def connectToFirstNode(self):
        if self.socketConnector.port != 10001:
            self.connect_with_node('localhost', 10001)

    # start a p2p node
    def startSocketCommunication(self):
        self.start()
        # also start discovery
        self.peerDiscoveryHandler.start()
        # connect to first node
        self.connectToFirstNode()

    # other nodes connect to us
    def inbound_node_connected(self, connected_node):
        self.peerDiscoveryHandler.handshake(connected_node)

    # we are connecting to other nodes
    def outbound_node_connected(self, connected_node):
        self.peerDiscoveryHandler.handshake(connected_node)

    # a callback that is invoked when a node send us a message
    def node_message(self, connected_node, message):
        message = Utils.decode(json.dumps(message))
        if message.messageType == 'DISCOVERY':
            self.peerDiscoveryHandler.handleMessage(message)

    # send a message to a peer
    def send(self, receiver, message):
        self.send_to_node(receiver, message)

    # broadcast a message to all of its peers
    def broadcast(self, message):
        self.send_to_nodes(message)
