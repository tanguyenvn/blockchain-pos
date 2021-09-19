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
        