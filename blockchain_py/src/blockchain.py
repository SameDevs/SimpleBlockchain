import datetime as date
from block import Block

# Generate genesis block
def createGenesisBlock():
  return Block(0, date.datetime.now(), {'proof-of-work': 9, 'transactions': []}, "0")

class Blockchain:
  def __init__(self):
    self.__transactions = []
    self.__blocks = []
    self.__blocks.append(createGenesisBlock())

  def addNewTransaction(self, sender, recipient, amount):
    newTransaction = {'sender': sender,  'recipient': recipient, 'amount': amount}
    self.__transactions.append(newTransaction)
    return newTransaction

  def proofOfWork(self):
    lastProof = self.__lastProofOfWork
    # Create a variable that we will use to find our next proof of work
    incrementor = lastProof + 1
    # Keep incrementing the incrementor until it's equal to a number divisible by 9 and the proof of work of the previous  block in the chain
    while not (incrementor % 9 == 0 and incrementor % lastProof == 0):
      incrementor += 1
    # Once that number is found,  we can return it as a proof of our work
    return incrementor

  def addNewBlockWithProof(self, proof):
    nBlockData = {'proof-of-work': proof, 'transactions': list(self.__transactions)}
    self.__transactions = []
    return self.__addNewBlockWithData(nBlockData)

  def getBlocksAsDictArray(self):
    return list(map(lambda block: block.toDict(), self.__blocks))

  def __addNewBlockWithData(self, data):
    lastBlock = self.__lastBlock
    nBlock = Block(lastBlock.index + 1, date.datetime.now(), data, lastBlock.hash)
    self.__blocks.append(nBlock)
    return nBlock

  @property
  def __lastProofOfWork(self):
    return self.__lastBlock.data['proof-of-work']

  @property
  def __lastBlock(self):
    return self.__blocks[-1]