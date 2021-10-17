class TransactionPool:
    def __init__(self):
        self.transactions = []
        self.threshold = 1

    # append a tractaction to the pool
    def addTransaction(self, transaction):
        self.transactions.append(transaction)

    # check if a transaction already exists in the pool
    def transactionExists(self, transaction):
        for tx in self.transactions:
            if tx.id == transaction.id:
                return True
        return False

    # remove a transaction from the pool after being added to blockchain
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

    # if the length of transaction list exceed a certain threshold, it's time to create a block
    def isForgerRequired(self):
        return len(self.transactions) >= self.threshold