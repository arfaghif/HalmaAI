from Pion import *
from Board import *
import math

class GameState():
    def __init__(self,board, listPionAgent=None, listPionPlayer=None, depth= 0):
        self.board = board
        if listPionAgent != None:
            self.listPionAgent = listPionAgent
        else:
            self.listPionAgent = []
            for pion in board.pions :
                if(pion.playerType == PlayerType.Agent):
                    self.listPionAgent.append(pion)
        if listPionPlayer != None:
            self.listPionPlayer = listPionPlayer 
        else:
            self.listPionPlayer = []
            for pion in board.pions :
                if(pion.playerType == PlayerType.Player):
                    self.listPionPlayer.append(pion)
        self.depth = depth
        for pion in self.listPionPlayer :
            board.canvas.tag_bind(pion.canvas, "<1>", lambda event, pion=pion: self.pion_on_click(pion))
        board.update()




    def isTerminalState(self):
        # isFill =False
        # for pion in self.listPionAgent:
        #     for tile in self.board.getAgentTiles():
        #         if pion.getPosition().isEqual(tile.getPosition()):
        #             isFill = True
        #             break
        #     if isFill == False:
        #             break
        # if isFill == True : return True
        # for pion in self.listPionPlayer:
        #     for tile in self.board.getPlayerTiles():
        #         if pion.getPosition().isEqual(tile.getPosition()):
        #             isFill = True
        #             break
        #     if isFill == False:
        #             break
        # return isFill
        return all(pion.isFinish() for pion in self.listPionAgent) or all(pion.isFinish() for pion in self.listPionPlayer)

    def utilityFunction(self):
        # value = 0
        # for pion in self.listPionAgent:
        #     distances = []
        #     for tile in self.board.getAgentTiles():
        #         distances.append(pion.getPosition().distance(tile.position()))
        #     if distances.min() != 0.0:
        #         value  += distances.max()
        # for pion in self.listPionPlayer:
        #     distances = []
        #     for tile in self.board.getPlayerTiles():
        #         distances.append(pion.getPosition().distance(tile.position()))
        #     if distances.min() != 0.0:
        #         value  -= distances.max()
        # return value
        pass

    
    def isThereAPion(self, position):
        # for pion in self.listPionAgent:
        #     if position.isEqual(pion.getPosition()):
        #         return 1
        # for pion in self.listPionPlayer:
        #     if position.isEqual(pion.getPosition()):
        #         return -1
        # return 0
        pass

    def validMovesAgent(self,listOfPion):
        validMoves = []
        for pion in listOfPion:
        #     if pion.isFinsih() : break
            x = pion.position[0]
            y = pion.position[1]
            # print(x,y)
            #up
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

            
        

                    # if isValidMove(pion,1,1):
                    #     validMoves.append([pion, Position(x+1,y+1)])
        #         else:
        #             validMoves += self.Rekursive([pion, 1, 1])

        #     #downright
        #     if (self.board.ValidPositon(x-1, y+1)):
            #     if not isThereAPion(self.position) :
            #         if isValidMove(pion,-1,1):
            #             validMoves.append([pion, Position(x-1,y+1)])
            #     else:
            #         validMoves += self.Rekursive([pion, -1 , 1]) 
            
            # #downleft
            # if (self.board.ValidPositon(x-1, y-1)):
            #     if not isThereAPion(self.position):
            #         if isValidMove(pion,-1,-1):
            #             validMoves.append([pion, Position(x-1,y-1)])
            #     else:
            #         validMoves += self.Rekursive(pion, -1, -1)
            # #upleft
            # if (self.board.ValidPositon(x+1, y+1)):
            #     if not isThereAPion(self.position):
            #         if isValidMove(pion,1,-1):
            #             validMoves.append(pion, Position(x+1,y-1))
            #     else:
            #         validMoves += self.Rekursive(pion,1, -1)

        return validMoves
            
    def pion_on_click(self, pion):
        # print("x")
        board.reset_tiles()
        valid_moves = self.validMovesAgent(self.listPionPlayer)
        # print(valid_moves)
        for valid_move in valid_moves:
            cell_width = int(board.canvas.winfo_width() / board.size)
            cell_height = int(board.canvas.winfo_height() / board.size)
            border_size = 5
            x1 = valid_move[1][0] * cell_width + border_size / 2
            y1 = valid_move[1][1] * cell_height + border_size / 2
            x2 = (valid_move[1][0] + 1) * cell_width - border_size / 2
            y2 = (valid_move[1][1] + 1) * cell_height - border_size / 2
            if valid_move[0] == pion :
                tile = board.tiles[valid_move[1][0]][valid_move[1][1]]
                board.canvas.itemconfig(tile.canvas, fill = "cyan", activefill ="magenta")
                board.canvas.tag_bind(tile.canvas, "<Button-1>", lambda event, pion=pion, position = tile.position: self.tile_on_click(pion,position))
        board.update()
    
    def tile_on_click(self,pion,position):
        board.reset_tiles()
        pion.set_position(position,board)
        self.next_turn()
        

    def next_turn(self):
        for pion in self.listPionPlayer :
            pion.set_hover(board,False)
            board.canvas.tag_unbind(pion.canvas, "<1>")
        board.update()
        temp = self.listPionAgent
        self.listPionAgent = self.listPionPlayer
        self.listPionPlayer = temp
        for pion in self.listPionPlayer :
            pion.set_hover(board,True)
            board.canvas.tag_bind(pion.canvas, "<1>", lambda event, pion=pion: self.pion_on_click(pion))
        board.update()
         

    def isValidMove(self, pion, x1, y1):
        x = pion.position[0] + x1
        y = pion.position[1] + y1
        #out of range
        if x<0 or x >= self.board.size or y <0 or y>= self.board.size :
            return False
        #there is another pion
        for pion in (self.listPionAgent + self.listPionPlayer):
            if pion.position == (x,y):
                return False
        
        return True
        

    def Rekursive(self, pion, x, y):
        # isOuterNest = pion.isOterNest()
        # isFinish = pion.isFinish()
        # xPion = pion.getPosition().getX()
        # yPion = pion.getPosition().getY()
        # validNextPos = self.board.ValidPositon(xPion + x*2+abs(x)/x,yPion + y*2+abs(y)/y) and not self.isThereAPion(xPion + x*2+abs(x)/x,yPion + y*2+abs(y)/y)
        # validPos = self.board.ValidPositon(xPion + x*2,yPion + y*2)
        # if validPos and not validNextPos and not (isFinish and self.board.tiles[xPion + x*2][yPion + y*2].getType() != pion.getType()*-1) and not (isOuterNest and self.board.tiles[xPion + x*2][yPion + y*2].getType() == pion.getType()):
        #     return [[pion,Position(xPion + x*2,yPion +y*2)]]
        # elif validPos and validNextPos:
        #     return [[pion,Position(x*2,y*2)]] + self.Rekursive(pion, x+abs(x)/x, y+abs(y)/y)
        # else:
        #     return []
        pass

    def minimax(self,depth, maks):
        # if self.isTerminalState(): return self.utilityFunction()
        
        # if maks :
        #     v = -math.inf
        #     for a in self.validMovesAgent(self.listPionAgent):
        #         gameState = GameState(self.listPionPlayer,self.listPionAgent, board, depth+1)
        #         v = max(v, gamestate.movePion(a[0], Position(a[1],a[2]))).minimax(depth, False)
        #     return v
        # else :
        #     v = math.inf
        #     for a in self.validMovesAgent(self.listPionAgent):
        #         gameState = GameState(self.listPionPlayer,self.listPionAgent, board, depth+1)
        #         v = min(v, gamestate.movePion(a[0], Position(a[1],a[2]))).minimax(depth, True)
        #     return v
        pass

    def minimaxAB(self,depth, maks,alpha,beta):
        # if self.isTerminalState(): return self.utilityFunction()
        
        # if maks :
        #     v = -math.inf
        #     for a in self.validMovesAgent(self.listPionAgent):
        #         gameState = GameState(self.listPionPlayer,self.listPionAgent, self.board, depth+1)
        #         v = max(v, gamestate.movePion(a[0], Position(a[1],a[2]))).minimax(depth, False,alpha,beta)
        #         if v >= beta: return v
        #         alpha = max(alpha,v)
        #     return v
        # else :
        #     v = math.inf
        #     for a in self.validMovesAgent(self.listPionAgent):
        #         gameState = GameState(self.listPionPlayer,self.listPionAgent, self.board, depth+1)
        #         v = min(v, gamestate.movePion(a[0], Position(a[1],a[2]))).minimax(depth, True, alpha,beta)
        #         if v <= alpha:return v
        #         alpha = min(beta,v)
        #     return v
        pass


board = Board(10)
newGame = GameState(board)
board.mainloop()