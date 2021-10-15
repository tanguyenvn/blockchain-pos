import json

import jsonpickle  # serialize object to JSON
from Crypto.Hash import SHA256


class Utils:
    @staticmethod
    def hash(data):
        dataString = json.dumps(data)
        dataBytes = dataString.encode('utf-8')
        dataHash = SHA256.new(dataBytes)
        return dataHash

    @staticmethod
    def encode(objectToEncode):
        return jsonpickle.encode(objectToEncode, unpicklable=True)

    @staticmethod
    def decode(encodedObject):
        return jsonpickle.decode(encodedObject)
