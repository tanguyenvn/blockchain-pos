from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

from Block import Block
from Transaction import Transaction
from Utils import Utils


class Wallet:
    def __init__(self):
        self.keyPair = RSA.generate(2048)

    def fromKey(self, file):
        key = ''
        with open(file, 'r') as keyfile:
            key = RSA.importKey(keyfile.read())
        self.keyPair = key

    # hash data, combine with keypair to sign it
    def sign(self, data):
        dataHash = Utils.hash(data)
        signatureSchemeObject = PKCS1_v1_5.new(self.keyPair)
        signature = signatureSchemeObject.sign(dataHash)
        return signature.hex()

    # validate signature of data is valid
    @staticmethod
    def isSignatureValid(data, hexSignature, pubKeyString):
        signature = bytes.fromhex(hexSignature)
        dataHash = Utils.hash(data)
        pubKey = RSA.importKey(pubKeyString)
        signatureSchemeObject = PKCS1_v1_5.new(pubKey)
        signatureValid = signatureSchemeObject.verify(dataHash, signature)
        return signatureValid

    # return public key of this wallet
    def getPubKeyString(self):
        pubKeyString = self.keyPair.publickey().exportKey('PEM').decode('utf-8')
        return pubKeyString

    def createTransaction(self, receiverPubKey, amount, type):
        transaction = Transaction(self.getPubKeyString(), receiverPubKey, amount, type)
        signature = self.sign(transaction.getPayload())
        transaction.sign(signature)
        return transaction

    def createBlock(self, transactions, lastHash, blockCount):
        block = Block(transactions, lastHash, self.getPubKeyString(), blockCount)
        signature = self.sign(block.payload())
        block.sign(signature)
        return block
