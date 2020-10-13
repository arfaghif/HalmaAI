from PlayerType import PlayerType
from position import Position

class Pion():
    def __init__(self, id, playerType, position, finish, board):
        self.id = id
        self.position = position
        self.playerType = playerType
        self.finish = False
        self.board = board

    def getPosition(self):
        return self.position

    def isFinish(self):
        return self.finish