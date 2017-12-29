import datetime as date
from block import Block

def create_genesis_block():
  return Block(0, date.datetime.now(), "Genesis Block", "0")

class Blockchain:
  def __init__(self):
    self.blocks = []
    self.blocks.append(create_genesis_block())

  def toDict(self):
    blocksArray = []
    for i in range(len(self.blocks)):
      block = self.blocks[i]
      blocksArray.append(block.toDict())
    return blocksArray