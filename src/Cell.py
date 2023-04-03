class Cell:

    def __init__(self, i, j, info):
        self.i = i
        self.j = j
        self.color, self.up, self.down, self.left, self.right = info
