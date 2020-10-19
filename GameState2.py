from Pion import *
from Board import *
import math
import time
from operator import itemgetter
from threading import Thread

class GameState():
    # Representasikan gamestate
    #---- dapat berupa game yang sedang berjalan
    #---- maupun virtualisasi dalam pengerjaan minimax
    def __init__(self, board, list_pion_player1=None, list_pion_player2=None, t_limit=60, p1='human', p2='minimax'):
        self.board = board
        self.list_pion_player1 = []
        for pion in self.board.pions :
            if(pion.player_number == PlayerNumber(1)):
                self.list_pion_player1.append(pion)
        
        self.list_pion_player2 = []
        for pion in self.board.pions :
            if(pion.player_number == PlayerNumber(2)):
                self.list_pion_player2.append(pion)

        self.computing = False
        self.t_limit = t_limit
        self.p1 = p1
        self.p2 = p2
        self.current_player = self.p1
        self.depth = 0

        # jika current_player adalah 'agent minimax'
        if (self.current_player=='minimax' or self.current_player=='minilocal'):
            self.execute_computer_move()

        else:
            if (self.current_player==self.p1):
                for pion in self.list_pion_player1 :
                    pion.set_hover(self.board,True)
                    self.board.canvas.tag_bind(pion.canvas, "<1>", lambda event, pion=pion: self.pion_on_click(pion))

                self.board.update()

            else: # self.current_player==p2
                for pion in self.list_pion_player2 :
                    pion.set_hover(self.board,True)
                    self.board.canvas.tag_bind(pion.canvas, "<1>", lambda event, pion=pion: self.pion_on_click(pion))

                self.board.update()

        # start tkInter
        self.board.mainloop()


    def isTerminalState(self):
        # Cek sudah ada di terminalstate
        # untested
        if all(pion.isFinish() for pion in self.list_pion_player1): return 1
        if all(pion.isFinish() for pion in self.list_pion_player2): return 2
        return 0

    def utilityFunction(self,player_number):
        # to do
        def point_distance(p1,p2):
            return ((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)
        
        if self.list_pion_player1[0].player_number == player_number:
            # print("lalalala")
            pions_agent = self.list_pion_player1
            pions_opp = self.list_pion_player2

        else:
            pions_agent = self.list_pion_player2
            pions_opp = self.list_pion_player1

        if pions_agent[0].player_number.value == 1 :
            # print("lulululu")
            target_agent = (self.board.size-1,self.board.size-1)
            target_opp = (0,0)
        else :
            # print("lulululu")
            target_agent = (0,0)
            target_opp = (self.board.size-1,self.board.size-1)
        

        val = 0
        for pion in pions_opp:
            if (pion.isFinish()) : continue
            dist = point_distance(pion.position,target_opp)
            val += dist

        for pion in pions_agent:
            if (pion.isFinish()) : continue
            dist = point_distance(pion.position,target_agent)
            val -= dist
        #value = 0
        return val


    
    def isThereAPion(self, x, y):
        # Kali aja butuh(?)
        for pion in (self.list_pion_player1 + self.list_pion_player2):
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

        #already in target
        # if self.isFinish() :
        #     if ( x == pion.position[0]*-1 and y == pion.position[1]*-1) : return False

        # #Still in base
        # if self.area==0:
        #     if not (self.isThereAPion(x,y)) : return True
        #     if not (x<0 or x >= self.board.size or y <0 or y>= self.board.size) : return True


        # #Neutral Ground
        # if self.area==1:
        #     if not (self.isThereAPion(x,y) and (x<0 or x>=self.board.size or y<0 or y>=self.board.size)): return True

        return True
    
    def validMovesAgent(self,listOfPion):
        # menghasilkan pergerakan pion yang valid dalam setiap gamestate
        # output berupa array dengan elemennya pasangan dari pion dan posisi tujuan
        validMoves = []
        for pion in listOfPion:
            x = pion.position[0]
            y = pion.position[1]
            #   up
            if self.isValidMove(pion,0,1):
                validMoves.append([pion, (x,y+1)])
            self.rekursive_move(pion,0,1,0,1,validMoves)
            #bottom
            if self.isValidMove(pion,0,-1):
                validMoves.append([pion, (x,y-1)])
            self.rekursive_move(pion,0,-1,0,-1,validMoves)
            #   right
            if self.isValidMove(pion,1,0):
                validMoves.append([pion, (x+1,y)])
            self.rekursive_move(pion,1,0,1,0,validMoves)
            #   left
            if self.isValidMove(pion,-1,0):
                validMoves.append([pion, (x-1,y)])
            self.rekursive_move(pion,-1,0,-1,0,validMoves)
            #   upright
            if self.isValidMove(pion,1,1):
                validMoves.append([pion, (x+1,y+1)])
            self.rekursive_move(pion,1,1,1,1,validMoves)
            #   bottomright
            if self.isValidMove(pion,1,-1):
                validMoves.append([pion, (x+1,y-1)])
            self.rekursive_move(pion,1,-1,1,-1,validMoves)
            #   upleft
            if self.isValidMove(pion,-1,1):
                validMoves.append([pion, (x-1,y+1)])
            self.rekursive_move(pion,-1,1,-1,1,validMoves)
            #   bottomleft
            if self.isValidMove(pion,-1,-1):
                validMoves.append([pion, (x-1,y-1)])
            self.rekursive_move(pion,-1,-1,-1,-1,validMoves)

        return validMoves
    
    def rekursive_move(self, pion, x1, y1,x2,y2, li):
        x = pion.position[0]
        y = pion.position[1]
        # base
        if (not self.isThereAPion(x+x1,y+y1) or (not self.isValidMove(pion, x1 + x2, y1 +y2)) or ([pion, (x + x1 +x2 , y + y1 + y2)] in li) ) : return
        # rec
        else:
            li.append([pion, (x + x1 +x2 , y + y1 + y2)])
            # self.rekursive_move(pion,x1 + 2*x2, y1 + 2*y2 ,li)
            # print("2", (x,y),(x + x1 +x2 , y + y1 + y2))
            # up
            self.rekursive_move(pion, x1 + x2, y1 + y2+1, 0, 1, li)
            # down
            self.rekursive_move(pion, x1 + x2, y1 + y2-1, 0,-1, li)
            # left
            self.rekursive_move(pion, x1 + x2-1, y1 + y2 , -1,0, li)
            # right
            self.rekursive_move(pion, x1 + x2 +1, y1 + y2 ,1,0, li)
            # upright
            self.rekursive_move(pion, x1 + x2+1 , y1 + y2+1,1,1  , li)
            # downright
            self.rekursive_move(pion, x1 + x2+1, y1 + y2-1,1,-1 ,li)
            # upleft
            self.rekursive_move(pion, x1 + x2-1, y1 + y2+1,-1,1 ,li)
            # downleft
            self.rekursive_move(pion, x1 + x2-1, y1 + y2-1 , -1,-1,li)
            
    def pion_on_click(self, pion):
        # Aksi ketika pion di klik
        # akan menampilkan pada antarmuka posisi valid yang dapat dipindahkan dari pion yang diklik

        if self.computing:
            return

        self.board.reset_tiles()

        if (self.current_player == self.p1):
            valid_moves = self.validMovesAgent(self.list_pion_player1)
        else:
            valid_moves = self.validMovesAgent(self.list_pion_player2)
        # for valid_move in valid_moves:
        #     print(valid_move[0].position,valid_move[1])

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

        if (self.current_player == self.p1):
            for pion in self.list_pion_player2 :
                pion.set_hover(self.board,False)
                self.board.canvas.tag_unbind(pion.canvas, "<1>")
        else:
            for pion in self.list_pion_player1 :
                pion.set_hover(self.board,False)
                self.board.canvas.tag_unbind(pion.canvas, "<1>")
        self.board.update()
        # print("self.current_player", self.current_player)
        self.current_player = (self.p1 if pion.player_number.value==1 else self.p2)
        print("self.current_player", self.current_player)
        
        self.execute_computer_move()
        
    
    def minimax(self,depth, maks, maks_depth, player_number):
        # minimax
        # untested
        if self.isTerminalState()!=0 or depth==maks_depth :
            return self.utilityFunction(player_number)

        # if (depth==2 and player_number==PlayerNumber.Player_2):
        #     print("hulahula")

        if (maks):
            v = -math.inf
        else : # not(maks)
            v = math.inf

        action = None

        if (player_number==PlayerNumber.Player_1):
            # if (depth==1):
            #     print("huluhulu")
            valid_moves = self.validMovesAgent(self.list_pion_player1)
        else:
            valid_moves = self.validMovesAgent(self.list_pion_player2)

        for validmove in valid_moves:
            # temp = [e for e in self.list_pion_player1 if e!=validmove[0]]

            # mendapatkan posisi dan area untuk dikembalikan seperti semula
            temp_position = validmove[0].position
            temp_area = validmove[0].area

            # if (depth==0):
            #     print("pion.position", validmove[0].position)

            x = validmove[1][0]
            y = validmove[1][1]
            pion = Pion(validmove[0].id, validmove[0].player_number,validmove[0].player_type,x,y)
            pion.set_area(self.board.tiles[x][y])

            # temp.append(pion)
            # gameState = GameState(self.board,self.list_pion_player2,temp,depth+1,True)

            # if (depth==0):
            #     print("pion.position", pion.position)

            # val = gameState.minimax(depth+1,not(maks),maks_depth,player_number)
            val = self.minimax(depth+1,not(maks),maks_depth, PlayerNumber.Player_1 
                if player_number==PlayerNumber.Player_2 else PlayerNumber.Player_2)

            if (depth==1):
                print("val", val)

            # mengembalikan posisi dan area pion menjadi semula
            pion.position = temp_position
            pion.area = temp_area

            if (maks):
                v = max(v, val)
            else: # not maks
                v = min(v, val)

            if depth==0 and val == v :
                action = validmove

        if (depth==0):
            self.action = action
            self.finish_execute = True
            return action
        else:
            return v

    def minimaxAB(self,depth, maks,alpha,beta,maks_depth,player_number):
        # minimax pruning
        # untested
        if self.isTerminalState()!=0 or depth==maks_depth : return self.utilityFunction(player_number)

        if(maks):
            v = -math.inf
            action = None
            for validmove in self.validMovesAgent(self.list_pion_player1):
                temp = [e for e in self.list_pion_player1 if e!=validmove[0]]
                x = validmove[1][0]
                y = validmove[1][1]
                pion = Pion(validmove[0].id, validmove[0].player_number,validmove[0].player_type,x,y)
                pion.set_area(self.board.tiles[x][y])
                temp.append(pion)
                gameState = GameState(self.board,self.list_pion_player2,temp,depth+1,True)
                val = gameState.minimaxAB(depth+1,False,alpha,beta,maks_depth,player_number)
                v = max (v, val )
                if(depth==0 and val == v) :
                    # masuk
                    action = validmove
                if v >= beta: return v
                alpha = max(alpha,v)

            if (depth==0):
                return action
            else:
                return v
        else:
            v = math.inf
            action = None
            for validmove in self.validMovesAgent(self.list_pion_player1):
                temp = [e for e in self.list_pion_player1 if e!=validmove[0]]
                x = validmove[1][0]
                y = validmove[1][1]
                pion = Pion(validmove[0].id, validmove[0].player_number,validmove[0].player_type,x,y)
                pion.set_area(self.board.tiles[x][y])
                temp.append(pion)
                gameState = GameState(self.board,self.list_pion_player2,temp,depth+1,True)
                val = gameState.minimaxAB(depth+1,True,alpha,beta,maks_depth,player_number)
                v = min (v, val )
                if(depth==0 and val == v) :
                    action = validmove
                if v <= alpha:return v
                beta = min(beta,v)
            if (depth==0):
                print("test")
                return action
            else:
                return v


    def local_search_minimax(self,depth, maks, maks_depth,player_number):
        # implement local search + minimax disini
        # return aksi ([pion,position])
        def point_distance2(p1,p2):
            return (p2[0]-p1[0])**2 + (p2[1]-p1[1])**2

        def heuristic_function(valid_move):
            if(valid_move[0].player_number.value == 1):
                target = (9,9)
            else:
                target = (0,0)
            x = valid_move[0].position[0]
            y = valid_move[0].position[1]
            return point_distance2((x,y),target) - point_distance2(valid_move[1],target)
        
        if self.isTerminalState()!=0 or depth==maks_depth : return self.utilityFunction(player_number)

        
        if (maks):
            v = -math.inf
        else : # not(maks)
            v = math.inf

        action = None
        valid_moves = self.validMovesAgent(self.list_pion_player1)
        valid_moves_value = [heuristic_function(valid_move) for valid_move in valid_moves]
        zipped_pairs = zip(valid_moves,valid_moves_value)
        valid_moves = [x for x,_ in sorted(zipped_pairs,  key = itemgetter(1), reverse=True)]

        for validmove in valid_moves[0:2]:
            temp = [e for e in self.list_pion_player1 if e!=validmove[0]]
                
            x = validmove[1][0]
            y = validmove[1][1]
            pion = Pion(validmove[0].id, validmove[0].player_number,validmove[0].player_type,x,y)
            pion.set_area(self.board.tiles[x][y])
            temp.append(pion)
            gameState = GameState(self.board,self.list_pion_player2,temp,depth+1,True)

            val = gameState.minimax(depth+1,not(maks),maks_depth,player_number)

            if (maks):
                v = max(v, val)
            else: # not maks
                v = min(v, val)

            if depth==0 and val == v :
                action = validmove

        if (depth==0):
            return action
        else:
            return v

    def time_counting(self):
        # become stop watch
        while(True):
            time.sleep(1)
            self.time_counter -= 1
            print(self.time_counter)

            if (self.time_counter == 0):
                self.time_out = True
                break

            elif(self.finish_execute):
                break

    def execute_computer_move(self):
        self.computing = True

        self.time_out = False
        self.finish_execute = False
        self.time_counter = self.t_limit
        self.board.draw_timer(self.time_counter)

        # t1 = Thread(target=self.time_counting, args=())
        # t1.start()
        if (self.current_player=='minimax'):
            if (self.current_player==self.p1):
                # t2 = Thread(target=self.minimax, args=(self.depth,True,3,self.list_pion_player1[0].player_number))
                t2 = self.minimax(self.depth,True,3,self.list_pion_player1[0].player_number)
            else:
                print("list_pion_player2[0].player_number", self.list_pion_player2[0].player_number)
                # t2 = Thread(target=self.minimax, args=(self.depth,True,3,self.list_pion_player2[0].player_number))
                t2 = self.minimax(self.depth,True,3,self.list_pion_player2[0].player_number)

        # jika current_player adalah 'agent minimax local search'
        if (self.current_player=='minilocal'):
            if (self.current_player==self.p1):
                act = self.minimax(self.depth,True,3,self.list_pion_player1[0].player_number) #TODO
            else:
                act = self.minimax(self.depth,True,3,self.list_pion_player2[0].player_number) #TODO

        # t1.start()
        # t2.start()

        # while not(self.time_out and self.finish_execute):
        #     time.sleep(0.1)
        #     self.board.draw_timer(self.time_counter)

        # t1.join()
        # t2.join()

        # jika selesai mengeksekusi
        if (self.finish_execute):
            pion = self.action[0]
            x = self.action[1][0]
            y = self.action[1][1]
            pion.set_position((x,y),self.board)
            pion.set_area(self.board.tiles[x][y])

            self.board.update()
            self.current_player = (self.p2 if pion.player_number.value==1 else self.p1)

        self.computing = False