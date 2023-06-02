import random
class Cell:
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False

class GamePole:
    def __init__(self, N, M):
        self.n = N
        self.m = M
        self.pole = [[Cell() for _ in range(N)] for _ in range(N)]

    def init(self):
        # выбираем случайно M точек для расстановки мин
        self.mines_coords = random.sample([(i, j) for i in range(self.N) for j in range(self.N)], self.M)
        # расставляем мины
        for x, y in self.mines_coords:
            self.pole[x][y].mine = True
        # считаем мины рядом
        for col in range(self.N):
            for row in range(self.N):
                self.pole[col][row].around_mines = self.get_mines(col, row)

    def get_mines(self, x, y):
        if self.pole[x][y].mine:
            res = -1
        else:
            res = 0

        for i in range(max(0, x - 1), min(x + 2, len(self.pole))):
            for j in range(max(0, y - 1), min(y + 2, len(self.pole))):
                if self.pole[i][j].mine:
                    res += 1
        return res

    def show(self):
        for row in self.pole:
            print(*map(lambda x: '#' if not x.fl_open else x.around_mines
                                        if not x.mine else '*', row)
                  )

pole_game = GamePole(10, 12)
pole_game.show()