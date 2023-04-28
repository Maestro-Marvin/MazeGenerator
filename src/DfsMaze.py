import random
from Interface import Interface
from Maze import Maze
from Cell import Cell


class DfsMaze(Maze):
    """разновидность лабиринта с построением dfs-ом"""

    def __init__(self, interface, height, width):
        """изначальная все клетки белого цвета"""
        super().__init__(interface, height, width)
        self.color = [[0 for j in range(self.m)] for i in range(self.n)]

    def gen(self):
        """построение начинается со случайной клетки"""
        i = random.randint(0, self.n - 1)
        j = random.randint(0, self.m - 1)
        self.dfs(i, j)

    def dfs(self, i, j):
        """Красим текущую клетку в серый цвет, перебираем её соседей
        в случайном порядке, если они ещё не посещены, то убираем стену между ними
        и запускаем dfs из соседей, после обработки клетки dfs-ом красим её в белый цвет"""
        self.color[i][j] = 3
        self.interface.draw_cell(self.make_cell(i, j))
        neighbors = [(i, j - 1), (i, j + 1), (i + 1, j), (i - 1, j)]
        random.shuffle(neighbors)
        for p in neighbors:
            i1, j1 = p
            if 0 <= i1 < self.n and 0 <= j1 < self.m and self.color[i1][j1] == 0:
                self.remove_wall(i, j, i1, j1)
                self.color[i][j] = 1
                self.interface.draw_cell(self.make_cell(i, j))
                self.dfs(i1, j1)
        self.color[i][j] = 2
        self.interface.draw_cell(self.make_cell(i, j))

    def make_cell(self, i, j):
        """Создаём клетку по её координатам, цвету и информации о стенах"""
        colors = ["WHITE", "GREY", "WHITE", "RED"]
        return Cell(i, j, [colors[self.color[i][j]], *self.cell_info(i, j)])
