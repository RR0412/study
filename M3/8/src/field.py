class Field:
    def __init__(self, size):
        self.size = size
        self.table = [['' for _ in range(size)] for _ in range(size)]

    def set_point(self, x: int, y: int, symbol: str) -> None:
        if not (0 <= x < self.size and 0 <= y < self.size):
            raise ValueError('Incorrect coordinates')
        if self.table[x][y]:
            raise ValueError('Cell is already taken')
        self.table[x][y] = symbol

    def __str__(self):
        result = f'{" ":3}' + ' '.join(f'{i:^3}' for i in range(self.size))
        for idx, row in enumerate(self.table):
            result += f'\n{idx:3}' + '|'.join(f'{elem:^3}' for elem in row)
        return result