from Utils import Utils

# A lot of a staker is for next block so it combines pubKey and lastBlockHash
class Lot:
    def __init__(self, pubKey, iteration, lastBlockHash):
        self.pubKey = str(pubKey)
        self.iteration = iteration # number of iterations
        self.lastBlockHash = lastBlockHash
        
    # Calculate hash of a lot
    def lotHash(self):
        hashData = self.pubKey + self.lastBlockHash
        for _ in range(self.iteration):
            hashData = Utils.hash(hashData).hexdigest()
        return hashData