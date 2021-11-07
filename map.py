
class MapNode:
  def __init__(self, f):
    self.dataval = f
    self.up = None
    self.down = None
    self.right = None
    self.left = None
    
  def insert (self, MapNode , direction):
    if direction == 1:
      self.up = MapNode
      MapNode.down = self
    elif direction == 2:
      self.right = MapNode
      MapNode.left = self
    elif direction == 3:
      self.left = MapNode
      MapNode.right = self
    elif direction == 4:
      self.down = MapNode
      MapNode.up = self

class Map:
  def __init__(self, f):
    self.Curr = f
  def goNext(self, input):
    if(input == 1):
      self.Curr = self.Curr.up
      return True
    elif(input == 2):
      self.Curr = self.Curr.right
      return True
    elif(input == 3):
      self.Curr = self.Curr.left
      return True
    elif(input == 4):
      self.Curr = self.Curr.down
      return True
    else:
      return False
