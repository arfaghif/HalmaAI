from PlayerNumber import PlayerNumber
from PlayerType import PlayerType

class Pion():
    # Representasikan pion pada papan halma
    def __init__(self, id, player_number, player_type, x_position, y_position,area= 0):
        self.position = (x_position, y_position)
        self.player_number = player_number
        self.player_type = player_type
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
    
    def set_area(self, tile):
        if(tile.typeTile.value==0):
            self.area = 1
        elif(self.player_number.value == tile.typeTile.value):
            self.area = 0
        else:
            self.area = 2
        


    def set_hover(self, board, hover):
        # set hover (feedback cursor pada button) pada pion 
        # hover = True jika ingin mengaktifkannya 
        if hover :
            board.canvas.itemconfig(self.canvas, activefill="cyan")
        else: 
            board.canvas.itemconfig(self.canvas, activefill=self.player_number.get_color())

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

        self.canvas = board.canvas.create_oval(x1, y1, x2, y2,tags="pion",  fill=self.player_number.get_color(),outline=None)
        