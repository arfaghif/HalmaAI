from PlayerType import PlayerType

class Pion():
    # Representasikan pion pada papan halma
    def __init__(self, id, playerType, x_position, y_position,area= 0):
        self.position = (x_position, y_position)
        self.playerType = playerType
        self.area = area

    def set_position(self, position,board):
        # set perubahan posisi pada pion 
        # secara back end maupun front end
        self.position = position
        cell_width = int(board.canvas.winfo_width() / board.size)
        cell_height = int(board.canvas.winfo_height() / board.size)
        border_size = 9
        
        x1 = self.position[0] * cell_width + border_size / 2
        y1 = self.position[1] * cell_height + border_size / 2
        x2 = (self.position[0] + 1) * cell_width - border_size / 2
        y2 = (self.position[1] + 1) * cell_height - border_size / 2

        board.canvas.coords(self.canvas,x1,y1,x2,y2)
        board.update()

    def set_hover(self, board, hover):
        # set hover (feedback cursor pada button) pada pion 
        # hover = True jika ingin mengaktifkannya 
        if hover :
            board.canvas.itemconfig(self.canvas, activefill="cyan")
        else: 
            board.canvas.itemconfig(self.canvas, activefill=self.playerType.get_color())

    def isFinish(self):
        # TRUE jika pion sudah berada di goal
        return self.area == 2

    def draw(self, board):
        # Menggambarkan pion ke antarmuka

        cell_width = int(board.canvas.winfo_width() / board.size)
        cell_height = int(board.canvas.winfo_height() / board.size)
        border_size = 9
        
        x1 = self.position[0] * cell_width + border_size / 2
        y1 = self.position[1] * cell_height + border_size / 2
        x2 = (self.position[0] + 1) * cell_width - border_size / 2
        y2 = (self.position[1] + 1) * cell_height - border_size / 2

        self.canvas = board.canvas.create_oval(x1, y1, x2, y2,tags="pion",  fill=self.playerType.get_color(),outline=None)
        