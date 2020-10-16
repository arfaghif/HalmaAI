from Pion import *
from Board import *
import math

class GameState():
    def __init__(self,listPionAgent, listPionPlayer, board, depth):
        self.listPionAgent = listPionAgent
        self.listPionPlayer = listPionPlayer
        self.board = board
        self.depth = depth

    def newGame():
        pass


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
        # validMoves = []
        # for pion in listOfPion:
        #     if pion.isFinsih() : break
        #     x = pion.getPosition().getX()
        #     y = pion.getPosition().getY()
        #     #upright
        #     if (self.board.ValidPositon(x+1, y+1)):
        #         if not isThereAPion(self.position):
        #             if isValidMove(pion,1,1):
        #                 validMoves.append([pion, Position(x+1,y+1)])
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

            # return validMoves
            pass

    def isValidMove(self, pion, x, y):
        # xPion = pion.getPosition().getX()
        # yPion = pion.getPosition().getY()
        # isOuterNest = pion.isOterNest()
        # isFinish = pion.isFinish()
        # return not (isFinish and self.board.tiles[xPion + x][yPion + y].getType() != pion.getType()*-1) and not (isOuterNest and self.board.tiles[xPion + x][yPion + y].getType() == TypeTile.Agent)
        pass

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