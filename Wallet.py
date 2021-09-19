from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

from Transaction import Transaction
from Utils import Utils


class Wallet():
    def __init__(self):
        self.keyPair = RSA.generate(2048)

    # hash data, combine with keypair to sign it
    def sign(self, data):
        dataHash = Utils.hash(data)
        signatureSchemeObject = PKCS1_v1_5.new(self.keyPair)
        signature = signatureSchemeObject.sign(dataHash)
        return signature.hex()
