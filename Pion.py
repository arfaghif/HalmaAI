from PlayerType import PlayerType

class Pion():
    def __init__(self, id, playerType, x_position, y_position, board, finish= False):
        self.id = id
        self.position = (x_position, y_position)
        self.playerType = playerType
        self.finish = finish
        self.board = board

    def getPosition(self):
        return self.position

    def isFinish(self):
        return self.finish