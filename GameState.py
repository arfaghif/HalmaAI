from Pion import *
from Board import *

class GameState():
    # Representasikan gamestate
    #---- dapat berupa game yang sedang berjalan
    #---- maupun virtualisasi dalam pengerjaan minimax
    def __init__(self, board, listPionAgent=None, listPionPlayer=None, depth= 0):
        self.board = board
        # deklarasi list pion player 1 dan 2
        #  saat next turn, satu sama lain akan ditukar
        if listPionAgent != None:
            self.listPionAgent = listPionAgent
        else:
            self.listPionAgent = []
            for pion in self.board.pions :
                if(pion.playerType == PlayerType.Agent):
                    self.listPionAgent.append(pion)
        if listPionPlayer != None:
            self.listPionPlayer = listPionPlayer 
        else:
            self.listPionPlayer = []
            for pion in self.board.pions :
                if(pion.playerType == PlayerType.Player):
                    self.listPionPlayer.append(pion)
        self.depth = depth

        # Setting pion dari player yang mendapat giliran untuk dapat ditekan untuk memilih aksi
        for pion in self.listPionPlayer :
            pion.set_hover(self.board,True)
            self.board.canvas.tag_bind(pion.canvas, "<1>", lambda event, pion=pion: self.pion_on_click(pion))

        self.board.update()

        # start tkInter
        self.board.mainloop()




    def isTerminalState(self):
        # Cek sudah ada di terminalstate
        # untested
        return all(pion.isFinish() for pion in self.listPionAgent) or all(pion.isFinish() for pion in self.listPionPlayer)

    def utilityFunction(self):
        # to do
        pass

    
    def isThereAPion(self, x, y):
        # Kali aja butuh(?)
        for pion in (self.listPionAgent + self.listPionPlayer):
            if pion.position == (x,y):
                return True
        return False

    def isValidMove(self, pion, x1, y1):
        # cek apakah tile perpindahan valid bagi si pion
        """
        to do :
        dilengkapi lagi syarat syaratnya seperti tidak dapat kembali ke sarang dsb
        """
        x = pion.position[0] + x1
        y = pion.position[1] + y1
        #out of range
        if x<0 or x >= self.board.size or y <0 or y>= self.board.size :
            return False
        #there is another pion
        if self.isThereAPion(x,y) : return False

        
        return True
    
    def validMovesAgent(self,listOfPion):
        # menghasilkan pergerakan pion yang valid dalam setiap gamestate
        # output berupa array dengan elemennya pasangan dari pion dan posisi tujuan
        """
        To do :
        Yang loncat loncat pion lain belum diimplementasikan
        """
        validMoves = []
        for pion in listOfPion:
            x = pion.position[0]
            y = pion.position[1]
            #   up
            if self.isValidMove(pion,0,1):
                validMoves.append([pion, (x,y+1)])
            #bottom
            if self.isValidMove(pion,0,-1):
                validMoves.append([pion, (x,y-1)])
            #   right
            if self.isValidMove(pion,1,0):
                validMoves.append([pion, (x+1,y)])
            #   left
            if self.isValidMove(pion,-1,0):
                validMoves.append([pion, (x-1,y)])
            #   upright
            if self.isValidMove(pion,1,1):
                validMoves.append([pion, (x+1,y+1)])
            #   bottomright
            if self.isValidMove(pion,1,-1):
                validMoves.append([pion, (x+1,y-1)])
            #   upleft
            if self.isValidMove(pion,-1,1):
                validMoves.append([pion, (x-1,y+1)])
            #   bottomleft
            if self.isValidMove(pion,-1,-1):
                validMoves.append([pion, (x-1,y-1)])

        return validMoves
            
    def pion_on_click(self, pion):
        # Aksi ketika pion di klik
        # akan menampilkan pada antarmuka posisi valid yang dapat dipindahkan dari pion yang diklik

        self.board.reset_tiles()
        valid_moves = self.validMovesAgent(self.listPionPlayer)

        for valid_move in valid_moves:
            if valid_move[0] == pion :
                # Untuk setiap tile yang valid akan diberi kemampuan button dan diterapkan juga hover
                tile = self.board.tiles[valid_move[1][0]][valid_move[1][1]]
                self.board.canvas.itemconfig(tile.canvas, fill = "cyan", activefill ="magenta")
                self.board.canvas.tag_bind(tile.canvas, "<Button-1>", lambda event, pion=pion, position = tile.position: self.tile_on_click(pion,position))
        self.board.update()
    
    def tile_on_click(self,pion,position):
        # Aksi etika tile di klik
        # Pion akan berpindah ke tile tujuan
        # dilakukan penonaktofkan tombol tile
        # Akan juga dilanjutkan turn nya ke lawan
        self.board.reset_tiles()
        pion.set_position(position,self.board)
        pion.set_area(self.board.tiles[position[0]][position[1]])
        self.next_turn()
        

    def next_turn(self):
        # nonaktifkan terlebih dahulu tombol pion player sebelumnya
        for pion in self.listPionPlayer :
            pion.set_hover(self.board,False)
            self.board.canvas.tag_unbind(pion.canvas, "<1>")
        self.board.update()
        temp = self.listPionAgent
        self.listPionAgent = self.listPionPlayer
        self.listPionPlayer = temp
        # mengaktifkan tombol player saat ini
        for pion in self.listPionPlayer :
            pion.set_hover(self.board,True)
            self.board.canvas.tag_bind(pion.canvas, "<1>", lambda event, pion=pion: self.pion_on_click(pion))
        self.board.update()
                 

    def Rekursive(self, pion, x, y):
        # Untuk rekursif valid move (?)
        pass

    def minimax(self,depth, maks):
        # minimax
        pass

    def minimaxAB(self,depth, maks,alpha,beta):
        # minimax pruning
        pass


