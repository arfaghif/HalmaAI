import tkinter as tk
from Tile import *
from Pion import *

class Board(tk.Tk):
    # Merepresentasikan board sebagai papan permainan. Papan permainan berupa GUI TkInter (inherrit)
    
    def __init__(self, size):
        tk.Tk.__init__(self)
        self.size = size
        self.canvas = tk.Canvas(self, width=550, height=550, bg="#fff",highlightthickness=0)
        self.canvas.grid(row=1, column=1, columnspan=self.size, rowspan=self.size)
        self.update()
        

        """
        Bagian ini literally copas 
        """
        label_font = "Helvetica 16"
        label_bg = "#fff"
        label_fg = "#333"
       
        for i in range(self.size):

            row_label1 = tk.Label(self, text=i + 1, font=label_font,
                bg=label_bg, fg=label_fg)
            row_label1.grid(row=i + 1, column=0)

            row_label2 = tk.Label(self, text=i + 1, font=label_font,
                bg=label_bg, fg=label_fg)
            row_label2.grid(row=i + 1, column=self.size + 2)

            col_label1 = tk.Label(self, text=chr(i + 97), font=label_font,
                bg=label_bg, fg=label_fg)
            col_label1.grid(row=0, column=i + 1)

            col_label2 = tk.Label(self, text=chr(i + 97), font=label_font,
                bg=label_bg, fg=label_fg)
            col_label2.grid(row=self.size + 2, column=i + 1)

        """
        Akhir bagian yang copas
        """

        # Representasikan papan yang terdiri dari kumpulan tile
        self.tiles = [[None]*size for i in range(size)]
        self.player1_tiles = []
        self.player2_tiles =[]
        self.pions = []
        id = 0
        for row in range(size):
            for col in range(size):
                if (row + col < 4):
                    tile = Tile(row,col, TypeTile(1))
                    self.player1_tiles.append(tile)
                    pion = Pion(id,PlayerNumber(1),PlayerType(1),row,col)
                    self.pions.append(pion)
                    id +=1
                elif row + col > 2 * (size - 3):
                    tile = Tile(row,col, TypeTile(2))
                    self.player2_tiles.append(tile)
                    pion = Pion(id,PlayerNumber(2),PlayerType(2),row,col)
                    self.pions.append(pion)
                    id +=1
                else:
                    tile = Tile(row,col, TypeTile(0))
                self.tiles[row] [col] = tile
                #gambarkan tile
                tile.draw(self)
               
        # gambarkan pion
        for pion in self.pions:
            pion.draw(self)
        self.update()


    def getAgentTiles(self):
        return self.agentTiles
    def getplayerTiles(self):
        return self.playerTiles

    def reset_tiles(self):
        # button pada semua tile dinonaktifkan termasuk hover buttonnya
        for i in range (self.size) :
            for j in range (self.size) :
                self.tiles[i][j].reset(self)


