from Wallet import Wallet
from Transaction import Transaction
from Wallet import Wallet

if __name__ == '__main__':
    # prepare a transaction
    sender = 'sender'
    receiver = 'receiver'
    amount = 1
    type = 'TRANSFER'
    transaction = Transaction(sender, receiver, amount, type)

    # sign transaction
    wallet = Wallet()
    signature = wallet.sign(transaction.toJson())
    print(signature)
