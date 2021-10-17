from Lot import Lot
from Utils import Utils

class ProofOfStake():
    def __init__(self):
        self.stakers = {}
        self.setGenesisNodeStaker()
    
    # init genesis staker
    def setGenesisNodeStaker(self):
        genesisPubKey = open('keys/genesisPublicKey.pem', 'r').read()
        self.stakers[genesisPubKey] = 1

    # update stake of a staker
    def update(self, pubKeyString, stake):
        if pubKeyString in self.stakers:
            self.stakers[pubKeyString] += stake
        else:
            self.stakers[pubKeyString] = stake
    
     # get stake of a staker
    def get(self, pubKeyString):
        if pubKeyString in self.stakers:
            return self.stakers[pubKeyString]
        else:
            return None

    # get all lots
    def getValidatorLots(self, seed):
        lots = []
        for validator in self.stakers.keys():
            # validator has more stake will have more lots
            for stake in range(self.get(validator)):
                lots.append(Lot(validator, stake+1, seed))
        return lots

    # determine whose lot is the winner
    # use probability: the one who has more lots will get higher chance to win
    def getWinnerLot(self, lots, seed):
        winnerLot = None
        leastOffset = None
        referenceHashIntValue = int(Utils.hash(seed).hexdigest(), 16) #hash to make random
        for lot in lots:
            lotIntValue = int(lot.lotHash(), 16)
            offset = abs(lotIntValue - referenceHashIntValue)
            if leastOffset is None or offset < leastOffset:
                leastOffset = offset
                winnerLot = lot
        return winnerLot

    # find the forger of the next block
    def getForger(self, lastBlockHash):
        lots = self.getValidatorLots(lastBlockHash)
        winnerLot: Lot = self.getWinnerLot(lots, lastBlockHash)
        return winnerLot.pubKey
