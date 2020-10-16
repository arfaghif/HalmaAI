
from TypeTile import TypeTile

class Tile():
    # Representasikan tile/ubin pada papan halma
    def __init__(self, x_position, y_position, typeTile):
        self.position =  (x_position,y_position)
        self.typeTile = typeTile

    def reset(self, board):
        # reset tombol dan hover
        board.canvas.itemconfig(self.canvas, fill=self.typeTile.get_color()[(sum(self.position))%2], activefill=self.typeTile.get_color()[(sum(self.position))%2])
        board.canvas.tag_unbind(self.canvas,"<Button-1>")

    def draw(self, board):
        # Menggambarkan tile ke antarmuka
        cell_width = int(board.canvas.winfo_width() / board.size)
        cell_height = int(board.canvas.winfo_height() / board.size)
        border_size = 5
        
        x1 = self.position[0] * cell_width + border_size / 2
        y1 = self.position[1] * cell_height + border_size / 2
        x2 = (self.position[0] + 1) * cell_width - border_size / 2
        y2 = (self.position[1] + 1) * cell_height - border_size / 2
        
        self.canvas = board.canvas.create_rectangle(x1, y1, x2, y2,tags="tile",  fill=self.typeTile.get_color()[(sum(self.position))%2], outline=None)
        