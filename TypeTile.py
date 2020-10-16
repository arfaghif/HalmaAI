from enum import Enum
class TypeTile(Enum):
    Free = 0
    AgentNest = 1
    PlayerNest = 2
    def get_color(self):
        if(self == TypeTile.Free):
            return ("#FFFFFF", "#D7D6D5")
        elif(self == TypeTile.AgentNest):
            return ("#F1392A","#E91F0F")
        else :
            return ("#0FE6E9","#078E90")
        
