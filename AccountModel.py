class AccountModel:
    def __init__(self):
        # keep tracks of pubKey of all participants in the network
        self.accounts = []
        self.balances = {}

    # add a new account using pubKey
    def addAccount(self, pubKeyString):
        if not pubKeyString in self.accounts:
            self.accounts.append(pubKeyString)
            self.balances[pubKeyString] = 0
    
    # get balance of an account using pubKey
    def getBalance(self, pubKeyString):
        if pubKeyString not in self.accounts:
            self.addAccount(pubKeyString)
        return self.balances[pubKeyString]

    # update balance of an account: amount can be positive/negative
    def updateBalance(self, pubKeyString, amount):
        if pubKeyString not in self.accounts:
            self.addAccount(pubKeyString)
        self.balances[pubKeyString] += amount
        
    