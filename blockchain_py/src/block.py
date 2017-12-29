import hashlib

class Block:
  def __init__(self, index, timestamp, data, previous_hash):
    self.index = index
    self.timestamp = timestamp
    self.data = data
    self.previous_hash = previous_hash
    self.hash = self.hash_block()

  def hash_block(self):
    block_description = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
    return hashlib.sha256(block_description.encode()).hexdigest()

  def toDict(self):
    return {"index": str(self.index), "timestamp": str(self.timestamp), "data": str(self.data), "hash": self.hash}