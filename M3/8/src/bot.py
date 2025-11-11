from player import Player
from field import Field

class Bot(Player):
    def make_move(self):
        for i, row in enumerate(self.field.table):
            for j, cell in enumerate(row):
                if cell == '':
                    print(f'Bot makes move to {i}, {j}')
                    self.field.set_point(i, j, self.symbol)
                    return