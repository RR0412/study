from field import Field

class Checker:
    def __init__(self, field: Field):
        self.field = field

    def check(self, player):
        
        for row in self.field.table:
            if all(cell == player.symbol for cell in row):
                return True

        
        for col in range(len(self.field.table)):
            if all(self.field.table[row][col] == player.symbol for row in range(len(self.field.table))):
                return True

        
        if all(self.field.table[i][i] == player.symbol for i in range(len(self.field.table))):
            return True
        if all(self.field.table[i][len(self.field.table)-1-i] == player.symbol for i in range(len(self.field.table))):
            return True

        return False