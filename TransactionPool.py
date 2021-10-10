class TransactionPool:
    def __init__(self):
        self.transactions = []

    def addTransaction(self, transaction):
        self.transactions.append(transaction)

    def transactionExists(self, transaction):
        for tx in self.transactions:
            if tx.id == transaction.id:
                return True
        return False

    def removeFromPool(self, transactions):
        newPoolTransactions = []
        for poolTx in self.transactions:
            insert = True
            for tx in transactions:
                if poolTx.equals(tx):
                    insert = False
            if insert == True:
                newPoolTransactions.append(poolTx)
        self.transactions = newPoolTransactions