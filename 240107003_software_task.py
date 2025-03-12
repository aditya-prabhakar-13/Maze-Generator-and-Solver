import pygame
import sys
import random
from collections import deque

# Maze config
ROWS, COLS = 21, 21
CELL_SIZE = 20
WIDTH, HEIGHT = COLS * CELL_SIZE, ROWS * CELL_SIZE

# Colors
WHITE  = (255, 255, 255)   # Path
BLACK  = (0, 0, 0)         # Walls
BLUE   = (0, 0, 255)       # BFS visited cells
RED    = (255, 0, 0)       # Final solution path
GREEN  = (0, 255, 0)       # Maze exit

def generate_maze(rows, cols):

    # Form a Maze with all walls.
    maze = [[1 for _ in range(cols)] for _ in range(rows)]
    start = (1, 1)
    maze[start[0]][start[1]] = 0
    stack = [start]
     
    directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
    
    while stack:
        current = stack[-1]
        x, y = current
        neighbors = []
         
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 < nx < rows - 1 and 0 < ny < cols - 1:
                if maze[nx][ny] == 1:
                    neighbors.append((nx, ny))
        if neighbors:
            next_cell = random.choice(neighbors)
            nx, ny = next_cell
             
            maze[(x + nx) // 2][(y + ny) // 2] = 0
            maze[nx][ny] = 0
            stack.append(next_cell)
        else:
            stack.pop()
    return maze

def draw_maze(maze, screen):

    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            color = WHITE if cell == 0 else BLACK
            pygame.draw.rect(screen, color, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.update()

def solve_maze(maze, start, end, screen):
     
    rows = len(maze)
    cols = len(maze[0])
    queue = deque()
    queue.append(start)
    came_from = {start: None}
    
    while queue:
        current = queue.popleft()
        if current == end:
            break
        x, y = current
        # Check 4-connected neighbors.
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if maze[nx][ny] == 0 and (nx, ny) not in came_from:
                    queue.append((nx, ny))
                    came_from[(nx, ny)] = current
                     
                    pygame.draw.rect(screen, BLUE, (ny * CELL_SIZE, nx * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                    pygame.display.update()
                    pygame.time.delay(10)
                    
     
    path = []
    current = end
    if current not in came_from:
        return None   
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    #path.reverse()
    return path

def draw_path(path, screen):
     
    for cell in path:
        x, y = cell
        pygame.draw.rect(screen, RED, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.display.update()
        pygame.time.delay(50)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("2D Maze Generator & Solver")
    
     
    maze = generate_maze(ROWS, COLS)
    draw_maze(maze, screen)
    
     
    start = (1, 1)
    end = (ROWS - 2, COLS - 2)
    
    pygame.draw.rect(screen, GREEN, (end[1] * CELL_SIZE, end[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.update()
    
     
    path = solve_maze(maze, start, end, screen)
    if path:
        draw_path(path, screen)
    else:
        print("No solution found!")
    
     
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
    sys.exit()

if True:
    main()
