from replit import db


class MapNode:
  dataval =""
  Up = None
  Down = None
  Right = None
  Left = None
  

  def __init__(self, f):
    self.dataval = f
    
  def print(self):
    return self.dataval
    
Home = MapNode("This is Home")
db["map"] = Home
Home.print

def output_map():
  return db[map].print

