import pygame
from Cell import Cell


class Interface:
    """Класс интерфейс, отрисовывает клетки для наглядного построения лабиринта
    задаются размеры окна, и цвета клеток в форматке RGB"""
    WIDTH, HEIGHT = 1000, 780
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Maze Generator")

    BLACK = (0, 0, 0)
    GREY = (128, 128, 128)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    WHITE = (255, 255, 255)
    FPS = 60

    def __init__(self, rows, cols):
        """Размер клеток подгоняется под размер окна"""
        self.rows = rows
        self.cols = cols
        self.side = min(self.WIDTH // cols, self.HEIGHT // rows)

    def draw_window(self):
        """Изначальная отрисовка окна, все клетки белые, все стены есть"""
        self.WIN.fill(self.WHITE)
        self.draw_grid()
        pygame.display.update()

    def draw_circle(self, cell):
        """Рисует круг внутри клетки"""
        y = cell[0] * self.side + self.side / 2
        x = cell[1] * self.side + self.side / 2
        pygame.draw.circle(self.WIN, cell[2], (x, y), self.side / 4)
        pygame.display.update()

    def draw_cell(self, cell):
        """Рисует клетку со всеми её стенами"""
        y, x = cell.i * self.side, cell.j * self.side
        colors = {"WHITE": self.WHITE, "RED": self.RED,
                  "GREY": self.GREY, "GREEN": self.GREEN}
        pygame.draw.rect(
            self.WIN, colors[cell.color], (x, y, self.side, self.side))
        walls_width = 3
        if cell.up:
            pygame.draw.line(self.WIN, self.BLACK, (x, y),
                             (x + self.side, y), walls_width)
        if cell.down:
            pygame.draw.line(self.WIN, self.BLACK, (x, y + self.side),
                             (x + self.side, y + self.side), walls_width)
        if cell.left:
            pygame.draw.line(self.WIN, self.BLACK, (x, y),
                             (x, y + self.side), walls_width)
        if cell.right:
            pygame.draw.line(self.WIN, self.BLACK, (x + self.side, y),
                             (x + self.side, y + self.side), walls_width)
        pygame.display.update()

    def draw_grid(self):
        """Рисует сетку на поле"""
        for i in range(self.rows):
            for j in range(self.cols):
                info = ["GREY", True, True, True, True]
                self.draw_cell(Cell(i, j, info))

    def pick_cell(self, time):
        """Пользователь выбирает начальную и конечную клетку для поиска пути между ними,
        стартовая клетка красится в зелёный, конечная в красный цвет"""
        if time > 2:
            return
        x, y = pygame.mouse.get_pos()
        i = y // self.side
        j = x // self.side
        if time == 1:
            self.start = (i, j)
            self.draw_circle((i, j, self.GREEN))
        if time == 2:
            self.finish = (i, j)
            self.draw_circle((i, j, self.RED))

    def main(self, maze, path):
        """Запускается построение лабиринта, далее пользователем выбираются клетки для нахождения пути между ними"""
        run = True
        clock = pygame.time.Clock()
        self.draw_window()
        maze.gen()
        time = 1
        used = False
        while run:
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.pick_cell(time)
                    time += 1
            if time > 2 and not used:
                path.find_path(self.start, self.finish)
                used = True
            pygame.display.flip()
        pygame.quit()
