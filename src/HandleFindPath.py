from Maze import Maze
from Cell import Cell
from Interface import Interface
from FindPath import FindPath
import pygame


class HandleFindPath:

    def __init__(self, maze, interface):
        self.maze = maze
        self.used = [[False for j in range(self.maze.m)] for i in range(self.maze.n)]
        self.interface = interface

    def handle_movement(self, cell, keys_pressed):
        i, j = cell
        if keys_pressed[pygame.K_LEFT] and j > 0 and self.maze.is_connected(i, j, i, j - 1):
            j -= 1
        elif keys_pressed[pygame.K_RIGHT] and j < self.maze.m - 1 and self.maze.is_connected(i, j, i, j + 1):
            j += 1
        elif keys_pressed[pygame.K_UP] and i > 0 and self.maze.is_connected(i, j, i - 1, j):
            i -= 1
        elif keys_pressed[pygame.K_DOWN] and i < self.maze.n - 1 and self.maze.is_connected(i, j, i + 1, j):
            i += 1
        return (i, j)

    def make_cell(self, i, j):
        colors = ["WHITE", "RED", "WHITE"]
        return Cell(i, j, [colors[self.used[i][j]], *self.maze.cell_info(i, j)])

    def reset(self):
        for i in range(self.maze.n):
            for j in range(self.maze.m):
                self.used[i][j] = False
                self.interface.draw_cell(self.make_cell(i, j))

    def find_path(self, start, finish):
        curr = start
        clock = pygame.time.Clock()
        flag = False
        while curr != finish:
            fps = 60
            clock.tick(fps)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        path = FindPath(self.maze, self.interface)
                        self.reset()
                        path.find_path(start, finish)
                        flag = True
                        break
                    i, j = curr
                    self.used[i][j] = True
                    keys_pressed = pygame.key.get_pressed()
                    curr = self.handle_movement(curr, keys_pressed)
                    i1, j1 = curr
                    if self.used[i1][j1]:
                        self.used[i][j] = False
                        self.interface.draw_cell(self.make_cell(i, j))
                    self.used[i1][j1] = True
                    self.interface.draw_cell(self.make_cell(i1, j1))
            if flag:
                break
