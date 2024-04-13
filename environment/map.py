import random

class Map:
    def __init__(self, size):
        self.size = size
        self.grid = [[' '] * size for _ in range(size)]

    def print_map(self):
        # Imprimir números das colunas acima do mapa
        print(' ', end='  ')
        for column in range(self.size):
            print(f'{column:2}', end='  ')
        print()

        # Imprimir mapa com números das linhas e células separadas por '|'
        for row in range(self.size):
            print(f'{row:2}|', end='')
            for column in range(self.size):
                print(f' {self.grid[row][column]}', end=' |')
            print()

    def generate_items(self, num_items1, num_items2):
        positions = random.sample([(x, y) for x in range(self.size) for y in range(self.size)],
                                 num_items1 + num_items2)
        for i in range(num_items1):
            x, y = positions[i]
            self.grid[x][y] = '1'
        for i in range(num_items1, num_items1 + num_items2):
            x, y = positions[i]
            self.grid[x][y] = '2'