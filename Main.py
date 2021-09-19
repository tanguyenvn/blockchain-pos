from Transaction import Transaction
from TransactionPool import TransactionPool
from Wallet import Wallet

if __name__ == '__main__':
    # create a wallet
    wallet = Wallet()

    # create a signed transaction
    receiver = 'receiver'
    amount = 1
    type = 'TRANSFER'
    transaction = wallet.createTransaction(receiver, amount, type)
    print(transaction.toJson())

    # validate transaction's signature
    isSignatureValid = wallet.isSignatureValid(transaction.getPayload(), transaction.signature, wallet.getPubKeyString())
    print(isSignatureValid)

    # create a fraudulent wallet
    fraudulentWallet = Wallet()
    isSignatureValid = wallet.isSignatureValid(transaction.getPayload(), transaction.signature, fraudulentWallet.getPubKeyString())
    print(isSignatureValid)

    # transaction pool
    transactionPool = TransactionPool()
    transactionPool.addTransaction(transaction)
    print(transactionPool.transactions)

