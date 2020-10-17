from enum import Enum

class PlayerNumber(Enum):
    Player_1 = 1
    Player_2 = 2
    def get_color(self):
        if(self.value == 1):
            return ("#0D7476")
        else :
            return ("#A20202")