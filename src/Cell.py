class Cell:
    """Структура данных для клетки лабиринта, содержит информацию о её положении (i, j), цвете и стенах"""

    def __init__(self, i, j, info):
        self.i = i
        self.j = j
        self.color, self.up, self.down, self.left, self.right = info
