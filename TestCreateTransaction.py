import requests

from Transaction import Transaction
from TransactionPool import TransactionPool
from Utils import Utils
from Wallet import Wallet

if __name__ == '__main__':
    bob = Wallet()
    alice = Wallet()
    exchange = Wallet()

    # Deposite 10 tokens to Alice
    tx = exchange.createTransaction(alice.getPubKeyString(), 10, 'EXCHANGE')

    # Submit transaction via API
    url = 'http://localhost:5001/transaction'
    package = {'transaction': Utils.encode(tx)}
    response = requests.post(url, json=package)
    print(response.text)