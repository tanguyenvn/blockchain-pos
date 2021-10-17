from ProofOfStake import ProofOfStake
from Lot import Lot
import string
import random

def testStake():
    pos = ProofOfStake()
    pos.update('bob', 10)
    pos.update('alice', 100)
    print(pos.get('bob'))
    print(pos.get('alice'))
    print(pos.get('jack'))    

def testLot():
    lot = Lot('bob', 1, 'lastBlockHash')
    print(lot.lotHash())

def getRandomString(length):
    letters = string.ascii_lowercase
    resultString = ''.join(random.choice(letters) for i in range(length))
    return resultString

def testForger(aliceStake: int, bobStake: int):
    # the higher stake a candidate puts, the higher chance it can become a forger
    pos = ProofOfStake()
    pos.update('alice', aliceStake)
    pos.update('bob', bobStake)

    bobWins = 0
    aliceWins = 0

    for i in range(100):
        lastBlockHash = getRandomString(i)
        forger = pos.getForger(lastBlockHash)
        if forger == 'bob':
            bobWins+=1
        elif forger == 'alice':
            aliceWins+=1

    print('alice stakes ' + str(aliceStake) + ', bob stakes ' + str(bobStake))
    print('alice won: ' + str(aliceWins) + ' times')
    print('bob won: ' + str(bobWins) + ' times')

if __name__ == '__main__':
    # testStake()
    # testLot()
    testForger(10, 100)
    testForger(100, 100)
