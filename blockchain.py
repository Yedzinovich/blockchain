#!usr/bin/python 
# -*- coding: utf-8 -*-

from hashlib import sha256

def updatehush(*args):
  hashing_text = ""; h = sha256()
  for arg in args:
    hashing_text +=str(arg)

  h.update(hashing_text.encode('utf-8')) 
  return h.hexdigest() 
  
class Block():
  data = None
  hash = None
  nonce = 0
  previous_hash = "0" * 64

  def __init__(self, data, number=0):
    self.data = data
    self.number = number

  def hash(self):
    return updatehush(
      self.previous_hash, 
      self.number, 
      self.data, 
      self.nonce
    ) 

  def __str__(self):
    return str(
       self.number, 
       self.hash(), 
       self.previous_hash, 
       self.data, 
       self.nonce
    )   

class Blockchain():
  difficilty = 4

  def __init__(self, chain=[]):
    self.chain = chain

  def add(self, block):
    self.chain.append({
      'hash':block.hash(), 
      'previous': block.previous_hash, 
      'number':block.number, 
      'data':block.data, 
      'nonce': block.nonce
      })  

  def mine(self, block):
    try:
      block.previous_hash = self.chain[-1].get('hash')
    except IndexError:
      pass

    while True:
      if block.hash()[:self.difficilty] == "0" * self.difficilty:
        self.add(block); break
      else:
        block.nonce +=1    

def main():
  
  #Testing
  blockchain = Blockchain()
  database = ["part1", "part2", "part3"]

  num = 0
  for data in database:
    num += 1
    blockchain.mine(Block(data, num))

  for block in blockchain.chain:
    print(block)

  
if __name__ == '__main__':
  main()   
