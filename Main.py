from Block import Block
from Transaction import Transaction
from TransactionPool import TransactionPool
from Wallet import Wallet
from Blockchain import Blockchain
from Utils import Utils

import pprint

if __name__ == '__main__':
    # create a wallet
    wallet = Wallet()

    # create a signed transaction
    receiver = 'receiver'
    amount = 1
    type = 'TRANSFER'
    transaction = wallet.createTransaction(receiver, amount, type)
    # print(transaction.toJson())

    # validate transaction's signature
    isSignatureValid = wallet.isSignatureValid(transaction.getPayload(), transaction.signature, wallet.getPubKeyString())
    # print(isSignatureValid)

    # create a fraudulent wallet
    fraudulentWallet = Wallet()
    isSignatureValid = wallet.isSignatureValid(transaction.getPayload(), transaction.signature, fraudulentWallet.getPubKeyString())
    # print(isSignatureValid)

    # transaction pool
    transactionPool = TransactionPool()
    if transactionPool.transactionExists(transaction) == False:
        transactionPool.addTransaction(transaction)
    # print(transactionPool.transactions)

    # create a blockchain
    blockchain = Blockchain()
    # pprint.pprint(blockchain.toJson())

    # create a block
    lastBlock = blockchain.blocks[-1]
    lastHash = Utils.hash(lastBlock.payload()).hexdigest()
    blockCount = lastBlock.blockCount + 1
    block = wallet.createBlock(transactionPool.transactions, lastHash, blockCount)
    # pprint.pprint(block.toJson())

    # validate block's signature
    isBlockSignatureValid = Wallet.isSignatureValid(block.payload(), block.signature, wallet.getPubKeyString())
    # print("isBlockSignatureValid", isBlockSignatureValid)
    isBlockSignatureValid = Wallet.isSignatureValid(block.payload(), block.signature, fraudulentWallet.getPubKeyString())
    # print("isBlockSignatureValid", isBlockSignatureValid)

    # validate if block is valid
    blockCountValid = blockchain.blockCountValid(block)
    lastBlockHashValid = blockchain.lastBlockHashValid(block)
    print('blockCountValid', blockCountValid)
    print('lastBlockHashValid', lastBlockHashValid)

    # add a block to blockchain
    if blockCountValid and lastBlockHashValid:
        blockchain.addBlock(block)
    pprint.pprint(blockchain.toJson())