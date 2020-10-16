from PlayerType import PlayerType

class Pion():
    def __init__(self, id, playerType, x_position, y_position,finish= False):
        self.position = (x_position, y_position)
        self.playerType = playerType
        self.finish = finish

    def getPosition(self):
        return self.position

    def isFinish(self):
        return self.finish

    def draw(self, board):
        cell_width = int(board.canvas.winfo_width() / board.size)
        cell_height = int(board.canvas.winfo_height() / board.size)
        border_size = 9
        
        x1 = self.position[0] * cell_width + border_size / 2
        y1 = self.position[1] * cell_height + border_size / 2
        x2 = (self.position[0] + 1) * cell_width - border_size / 2
        y2 = (self.position[1] + 1) * cell_height - border_size / 2
        
        if(self.playerType==PlayerType.Player):
            active_fill = 'cyan'
        else:
            active_fill = None

        self.canvas = board.canvas.create_oval(x1, y1, x2, y2,tags="pion",  fill=self.playerType.get_color(), activefill=active_fill,  outline=None)
        