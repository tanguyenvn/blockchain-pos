import copy
import time
import uuid


class Transaction:
    def __init__(self, senderPubKey, receiverPubKey, amount, type):
        self.senderPubKey = senderPubKey
        self.receiverPubKey = receiverPubKey
        self.amount = amount
        self.type = type

        self.id = uuid.uuid1().hex
        self.timestamp = time.time()
        self.signature = ''
    
    def toJson(self):
        return self.__dict__
    
    def getPayload(self):
        payload = copy.deepcopy(self.toJson())
        payload['signature'] = ''
        return payload

    def sign(self, signature):
        self.signature = signature

    def equals(self, transaction):
        if self.id == transaction.id:
            return True
        return False
