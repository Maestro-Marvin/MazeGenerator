from Maze import Maze
from Cell import Cell
from Interface import Interface
import random


class FindPath:
    """Автоматический поиск пути в лабиринте между клетками с помощью dfs"""

    def __init__(self, maze, interface):
        """изначальная все клетки белого цвета"""
        self.maze = maze
        self.color = [[0 for j in range(self.maze.m)]
                      for i in range(self.maze.n)]
        self.interface = interface

    def make_cell(self, i, j):
        """Создаём клетку по её координатам, цвету и информации о стенах,
        начальная клетка зелёного цвета, конечная красного"""
        colors = ["WHITE", "RED", "GREY", "GREEN", "WHITE"]
        return Cell(i, j, [colors[self.color[i][j]], *self.maze.cell_info(i, j)])

    def find_path(self, start, finish):
        """Поиск пути между стартовой и конечной клеткой"""
        try:
            self.dfs(start, start, finish)
        except:
            pass

    def dfs(self, start, curr, finish):
        """Текущая клетка красится в красный цвет, если она стратовая то в зелёный,
        если мы уже попали в конечную клетку, то бросается исключение, которое ловится в
        find_path, это сделано, чтобы не выполнять перекрашивания после обработки вершины dfs-ом
        далее перебираем соседей в случайном порядке, если они ещё не посещены, то убираем стену между ними,
        перекрашиваем клетку в серый и запускаем dfs из соседей, после обработки клетки dfs-ом красим её в белый цвет"""
        i, j = curr
        self.color[i][j] = 1
        if curr == start:
            self.color[i][j] = 3
        self.interface.draw_cell(self.make_cell(i, j))
        if curr == finish:
            raise
        neighbors = [(i, j - 1), (i, j + 1), (i + 1, j), (i - 1, j)]
        random.shuffle(neighbors)
        for p in neighbors:
            i1, j1 = p
            if 0 <= i1 < self.maze.n and 0 <= j1 < self.maze.m and self.color[i1][j1] == 0 and \
                    self.maze.is_connected(i, j, i1, j1):
                if curr != start:
                    self.color[i][j] = 2
                    self.interface.draw_cell(self.make_cell(i, j))
                self.dfs(start, p, finish)
        self.color[i][j] = 4
        self.interface.draw_cell(self.make_cell(i, j))
