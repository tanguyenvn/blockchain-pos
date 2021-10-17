import requests

from Transaction import Transaction
from TransactionPool import TransactionPool
from Utils import Utils
from Wallet import Wallet


def submitTransaction(sender: Wallet, receiver: Wallet, amount, type):
    # prepare transaction
    tx = sender.createTransaction(receiver.getPubKeyString(), amount, type)

    # submit transaction via API
    url = 'http://localhost:5001/transaction'
    payload = {'transaction': Utils.encode(tx)}
    response = requests.post(url, json=payload)
    print(response.text)

if __name__ == '__main__':
    bob = Wallet()
    alice = Wallet()
    exchange = Wallet()

    tx = submitTransaction(exchange, alice, 100, 'EXCHANGE')
    tx = submitTransaction(exchange, bob, 100, 'EXCHANGE')
    tx = submitTransaction(alice, alice, 25, 'STAKE')
