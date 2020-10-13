from Tile import *

class Board():
    def __init__(self, size):
        self.size = size
        self.tiles = [[None]*size for i in range(size)]
        self.agentTiles = []
        self.playerTiles =[]
        for row in range(size):
            for col in range(size):
                if (row + col < 4):
                    tile = Tile(Position(row,col), TypeTile(1))
                    self.agentTiles.append(tile)
                elif row + col > 2 * (size - 3):
                    tile = Tile(Position(row,col), TypeTile(2))
                    self.playerTiles.append(tile)
                else:
                    tile = Tile(Position(row,col), TypeTile(0))
                self.tiles[row] [col] = tile
    def getAgentTiles(self):
        return self.agentTiles
    def getplayerTiles(self):
        return self.playerTiles