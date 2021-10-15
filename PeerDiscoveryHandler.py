import threading
import time

from Message import Message
from Utils import Utils


# discovery new peers
class PeerDiscoveryHandler:
    def __init__(self, node):
        self.socketCommunication = node #???

    # start peer discovery proccess
    def start(self):
        statusThread = threading.Thread(target=self.status, args=())
        statusThread.start()

        discoveryThread = threading.Thread(target=self.discovery, args=())
        discoveryThread.start()

    # signal current status
    def status(self):
        while True:
            print('Current connections:')
            for peer in self.socketCommunication.peers:
                print(str(peer.ip) + ':' + str(peer.port))
            time.sleep(10)
    
    # broadcast to other nodes to get more new peers
    def discovery(self):
        while True:
            handshakeMessage = self.handshakeMessage()
            self.socketCommunication.broadcast(handshakeMessage)
            time.sleep(10)

    def handshake(self, connected_node):
        handshakeMessage = self.handshakeMessage()
        self.socketCommunication.send(connected_node, handshakeMessage)

    def handshakeMessage(self):
        ownConnector = self.socketCommunication.socketConnector
        ownPeers = self.socketCommunication.peers
        data = ownPeers
        messageType = 'DISCOVERY'
        message = Message(ownConnector, messageType, data)
        encodedMessage = Utils.encode(message)
        return encodedMessage

    # handle handshake message
    def handleMessage(self, message: Message):
        peerSocketConnector = message.senderConnector
        isNewPeer = True
        for peer in self.socketCommunication.peers:
            if peer.equals(peerSocketConnector):
                isNewPeer = False
        if isNewPeer:
            self.socketCommunication.peers.append(peerSocketConnector)
            
        peersOfPeers = message.data
        for peerOfPeer in peersOfPeers:
            isPeerKnown = False
            for peer in self.socketCommunication.peers:
                if peer.equals(peerOfPeer):
                    isPeerKnown = True
            if not isPeerKnown and not peerOfPeer.equals(self.socketCommunication.socketConnector):
                self.socketCommunication.peers.append(peerOfPeer)

