from Interface import Interface


class Maze:
    """Абстрактный класс - Maze, представляющий базовый функционал, 
    от которого наследуются DfsMaze и KruskalMaze"""

    def __init__(self, interface, height, width):
        """Для каждой клетки достаточно хранить её правую и нижнюю стену"""
        self.interface = interface
        self.n = height
        self.m = width
        self.right_bound = [
            [True for j in range(width)] for i in range(height)]
        self.lower_bound = [
            [True for j in range(width)] for i in range(height)]

    def remove_wall(self, i1, j1, i2, j2):
        """Удаляет стену между соседними клетками"""
        if i1 == i2 and j1 - 1 == j2:
            self.right_bound[i2][j2] = False
        elif i1 == i2 and j1 + 1 == j2:
            self.right_bound[i1][j1] = False
        elif i1 - 1 == i2 and j1 == j2:
            self.lower_bound[i2][j2] = False
        elif i1 + 1 == i2 and j1 == j2:
            self.lower_bound[i1][j1] = False

    def is_connected(self, i1, j1, i2, j2):
        """Проверяет что две клетки соседнии"""
        if i1 == i2 and j1 - 1 == j2 and not self.right_bound[i2][j2]:
            return True
        if i1 == i2 and j1 + 1 == j2 and not self.right_bound[i1][j1]:
            return True
        if i1 - 1 == i2 and j1 == j2 and not self.lower_bound[i2][j2]:
            return True
        if i1 + 1 == i2 and j1 == j2 and not self.lower_bound[i1][j1]:
            return True
        return False

    def cell_info(self, i, j):
        """Возвращает информацию о четрёх стенах клетки"""
        ans = [False, False, False, False]
        if i == 0 or (i != 0 and self.lower_bound[i - 1][j]):
            ans[0] = True
        if self.lower_bound[i][j]:
            ans[1] = True
        if j == 0 or (j != 0 and self.right_bound[i][j - 1]):
            ans[2] = True
        if self.right_bound[i][j]:
            ans[3] = True
        return ans

    def print_maze(self):
        """Выводит лабиринт в консоль"""
        print("_" * (4 * self.m + 1))
        for i in range(self.n):
            ans = "|"
            for j in range(self.m):
                ans += "___" if self.lower_bound[i][j] else "   "
                ans += "|" if self.right_bound[i][j] else " "
            print(ans)
