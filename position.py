import math

class Position ():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def isSamePosition(self, position):
        self.getX() == position.getX() and self.getY() == self.getY()
