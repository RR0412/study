from field import Field


class Player:
    def __init__(self, symbol: str, field: Field):
        self.symbol = symbol
        self.field = field

    def make_move(self):
        while True:
            try:
                x = int(input('x: '))
                y = int(input('y: '))
            except ValueError:
                print('Invalid coordinates, enter numbers!')
                continue
            try:
                self.field.set_point(x, y, self.symbol)
            except ValueError as exc:
                print(exc)
            else:
                break