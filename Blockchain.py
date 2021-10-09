from Block import Block
from Utils import Utils

class Blockchain:
    def __init__(self):
        # add genesis block
        self.blocks = [Block.genesis()]

    # add a block to blockchain
    def addBlock(self, block):
        self.blocks.append(block)
    
    def toJson(self):
        data = {}
        jsonBlocks = []
        for block in self.blocks:
            jsonBlocks.append(block.toJson())
        data['blocks'] = jsonBlocks
        return data

    # validate if blockCount matches with the number of added blocks in blockchain
    def blockCountValid(self, block):
        return self.blocks[-1].blockCount == block.blockCount - 1

    # validate if the prev hash is the last block's hash in blockchain
    def lastBlockHashValid(self, block):
        lastBlockHash = Utils.hash(self.blocks[-1].payload()).hexdigest()
        return block.lastHash == lastBlockHash
