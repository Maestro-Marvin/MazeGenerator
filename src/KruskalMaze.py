from Maze import Maze
from Cell import Cell
import random
from Interface import Interface


class KruskalMaze(Maze):

    def __init__(self, interface, height, width):
        super().__init__(interface, height, width)
        self.parent = [[-1 for j in range(self.m)] for i in range(self.n)]
        self.size = [[1 for j in range(self.m)] for i in range(self.n)]
        self.edges = []
        for i in range(self.n):
            for j in range(self.m):
                neighbors = [(i, j - 1), (i, j + 1), (i + 1, j), (i - 1, j)]
                for i1, j1 in neighbors:
                    if 0 <= i1 < self.n and 0 <= j1 < self.m:
                        self.edges.append(((i, j), (i1, j1)))

    def root(self, cell):
        i, j = cell
        if self.parent[i][j] == -1:
            return cell
        self.parent[i][j] = self.root(self.parent[i][j])
        return self.parent[i][j]

    def unite(self, u, v):
        u, v = self.root(u), self.root(v)
        if u == v:
            return
        i1, j1 = u
        i2, j2 = v
        if self.size[i1][j1] > self.size[i2][j2]:
            self.parent[i2][j2] = u
            self.size[i1][j1] = max(self.size[i1][j1], self.size[i2][j2] + 1)
        else:
            self.parent[i1][j1] = v
            self.size[i2][j2] = max(self.size[i2][j2], self.size[i1][j1] + 1)

    def make_cell(self, i, j):
        return Cell(i, j, ["WHITE", *self.cell_info(i, j)])

    def gen(self):
        random.shuffle(self.edges)
        for e in self.edges:
            u, v = e
            if self.root(u) != self.root(v):
                self.unite(u, v)
                self.remove_wall(u[0], u[1], v[0], v[1])
                self.interface.draw_cell(self.make_cell(u[0], u[1]))
                self.interface.draw_cell(self.make_cell(v[0], v[1]))
