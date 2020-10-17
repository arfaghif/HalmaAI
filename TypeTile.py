from enum import Enum
class TypeTile(Enum):
    Free = 0
    Player_1_Nest = 1
    Player_2_Nest = 2
    def get_color(self):
        if(self.value == 0):
            return ("#FFFFFF", "#D7D6D5")
        elif(self.value == 1):
            return ("#F1392A","#E91F0F")
        else :
            return ("#0FE6E9","#078E90")
        
