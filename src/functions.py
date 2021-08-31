def index(i, j, cols):
    if i < 0 or j < 0 or i >= cols or j >= cols:
        return -1
    return i*cols + j

class Cell:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.walls = [True for i in range(4)]
        self.visited = False

    def checkNeighbors(self, grid, cols):
        from random import randint
        ind = index(self.i, self.j-1, cols)
        allNeighbors = []
        if ind != -1:
            top     = grid[index(self.i, self.j-1, cols)]
            allNeighbors.append(top)
        ind = index(self.i+1, self.j, cols)
        if ind != -1:
            right   = grid[index(self.i+1, self.j, cols)]
            allNeighbors.append(right)
        ind = index(self.i, self.j+1, cols)
        if ind != -1:
            bottom  = grid[index(self.i, self.j+1, cols)]
            allNeighbors.append(bottom)
        ind = index(self.i-1, self.j, cols)
        if ind != -1:
            left    = grid[index(self.i-1, self.j, cols)]
            allNeighbors.append(left)
        neighbors       = []
        for neigh in allNeighbors:
            if not neigh.visited and neigh:
                neighbors.append(neigh)
        nNeighbors = len(neighbors)
        if nNeighbors > 0:
            r = randint(0, nNeighbors-1)
            return neighbors[r]
        # elif nNeighbors == 0:



    def show(self, screen, w):
        import pygame
        white = (255, 255, 255)
        x = self.i*w
        y = self.j*w
        if self.visited:
            surf = pygame.Surface((w, w))
            surf.fill((255, 0, 255, 100))
            screen.blit(surf, (x, y))

        if self.walls[0]:
            pygame.draw.line(screen, white, (x  , y), (x+w, y))
        if self.walls[1]:
            pygame.draw.line(screen, white, (x+w, y), (x+w, y+w))
        if self.walls[2]:
            pygame.draw.line(screen, white, (x+w, y+w), (x, y+w))
        if self.walls[3]:
            pygame.draw.line(screen, white, (x, y+w), (x, y))


    def highlight(self, screen, w):
        import pygame
        white = (255, 255, 255)
        x = self.i*w
        y = self.j*w
        if self.visited:
            surf = pygame.Surface((w, w))
            surf.fill((0,0,255, 100))
            screen.blit(surf, (x, y))

        if self.walls[0]:
            pygame.draw.line(screen, white, (x  , y), (x+w, y))
        if self.walls[1]:
            pygame.draw.line(screen, white, (x+w, y), (x+w, y+w))
        if self.walls[2]:
            pygame.draw.line(screen, white, (x+w, y+w), (x, y+w))
        if self.walls[3]:
            pygame.draw.line(screen, white, (x, y+w), (x, y))

def removeWall(a, b):
    x = a.i - b.i
    if x == 1:
        a.walls[3] = False
        b.walls[1] = False
    elif x == -1:
        a.walls[1] = False
        b.walls[3] = False
    y = a.j - b.j
    if y == -1:
        a.walls[2] = False
        b.walls[0] = False
    elif y == 1:
        a.walls[0] = False
        b.walls[2] = False

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
    from pygame.time import delay
    WIDTH = 500
    HEIGHT = 500
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    cols    = 20
    rows    = 20
    w       = WIDTH/cols
    grid    = createGrid(cols, rows)
    current = grid[0]
    stack   = []
    # Running
    running = True
    while running:
        screen.fill(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        current.visited = True
        next = current.checkNeighbors(grid, cols)
        if next:
            next.visited = True
            stack.append(current)
            removeWall(current, next)
            current = next

        showGrid(grid, screen, w)
        current.highlight(screen, w)

        pygame.display.update()
