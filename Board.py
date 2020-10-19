import tkinter as tk
from Tile import *
from Pion import *
import threading
import time

class Board(tk.Tk):
    # Merepresentasikan board sebagai papan permainan. Papan permainan berupa GUI TkInter (inherrit)
    
    def __init__(self, size,t):
        tk.Tk.__init__(self)
        self.title("Halma MiniMax")
        self.size = size
        self.maks_time = t
        self.canvas = tk.Canvas(self, width=550, height=550, bg="white",highlightthickness=0)
        self.canvas.grid(row=1, column=1, columnspan=self.size, rowspan=self.size)
        self.update()
        self.configure(background = '#839192')
        

        # Set GUI label pada papan permainan
        label_font = "Arial 16"
        label_bg = "#839192"
        label_fg = "#000000"
       
        for i in range(self.size):
            left_label = tk.Label(self, text=i + 1, font=label_font, bg=label_bg, fg=label_fg)
            left_label.grid(row=i + 1, column=0)

            right_label = tk.Label(self, text=i + 1, font=label_font,bg=label_bg, fg=label_fg)
            right_label.grid(row=i + 1, column=self.size + 2)

            up_label = tk.Label(self, text=chr(i + 97), font=label_font,bg=label_bg, fg=label_fg)
            up_label.grid(row=0, column=i + 1)

            bottom_label = tk.Label(self, text=chr(i + 97), font=label_font,bg=label_bg, fg=label_fg)
            bottom_label.grid(row=self.size + 2, column=i + 1)

        
        # Membuatat label di bawah untuk set giliran
        self.canvas2 = tk.Canvas(self, width=600, height=50, bg="white",highlightthickness=0)
        self.label = tk.Label(self, text= "Player 1 TURN", font=label_font, bg='white', fg=label_fg)
        self.canvas2.grid(row=self.size + 3, column=0, columnspan =self.size + 3)
        self.label.grid(row=self.size + 3, column=0, columnspan = self.size + 3)


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
                    pion = Pion(id,PlayerNumber(1),PlayerType(2),row,col)
                    self.pions.append(pion)
                    id +=1
                elif row + col > 2 * (size - 3):
                    tile = Tile(row,col, TypeTile(2))
                    self.player2_tiles.append(tile)
                    pion = Pion(id,PlayerNumber(2),PlayerType(3),row,col)
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



    def reset_tiles(self):
        # button pada semua tile dinonaktifkan termasuk hover buttonnya
        for i in range (self.size) :
            for j in range (self.size) :
                self.tiles[i][j].reset(self)

    def countdown(self,waktu,player):
        # untuk hitung mundur AI
        self.timeout = waktu
        while self.timeout > 0:
            time.sleep(1)
            self.timeout -= 1

    def create_thread(self,player):
        # membuat thread hitung mundur
        self.thread_timer = threading.Thread(target=self.countdown,args=(self.maks_time,player))
        self.thread_timer.start()

    def stop_thread(self):
        # memberhentikan thead hitung mundur
        self.timeout = 0
        self.thread_timer.join()
