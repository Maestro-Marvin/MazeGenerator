from Maze import Maze
from Cell import Cell
from Interface import Interface
import random

class FindPath:

    def __init__(self, maze, interface):
        self.maze = maze
        self.color = [[0 for j in range(self.maze.m)] for i in range(self.maze.n)]
        self.interface = interface

    def make_cell(self, i, j):
        colors = ["WHITE", "RED", "GREY", "GREEN", "WHITE"]
        return Cell(i, j, [colors[self.color[i][j]], *self.maze.cell_info(i, j)])

    def find_path(self, start, finish):
        try:
            self.dfs(start, start, finish)
        except:
            pass

    def dfs(self, start, curr, finish):
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