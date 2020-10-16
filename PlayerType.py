from enum import Enum

class PlayerType(Enum):
    Agent = 1
    Player = -1
    def get_color(self):
        if(self == PlayerType.Agent):
            return ("#0D7476")
        else :
            return ("#A20202")