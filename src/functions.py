class Cell:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self, screen, w):
        import pygame
        white = (255, 255, 255)
        x = self.i*w
        y = self.j*w
        pygame.draw.line(screen, white, (x  , y), (x+w, y))
        pygame.draw.line(screen, white, (x+w, y), (x+w, y+w))
        pygame.draw.line(screen, white, (x+w, y+w), (x, y+w))
        pygame.draw.line(screen, white, (x, y+w), (x, y))

def createGrid(cols, rows):
    grid = []
    for i in range(rows):
        for j in range(cols):
            grid.append(Cell(i, j))
    return grid

def showGrid(grid, screen, w):
    for cell in grid:
        cell.show(screen, w)

def start():
    import pygame
    WIDTH = 500
    HEIGHT = 500
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    cols    = 20
    rows    = 20
    w       = WIDTH/cols
    grid    = createGrid(cols, rows)

    running = True
    while running:
        screen.fill(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        showGrid(grid, screen, w)
        pygame.display.update()
