import pygame
import heapq
import sys
import time

# Define los colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH, HEIGHT = 220, 100
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bidirectional A*")
maze = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

maze[1][0] = 1
maze[2][0] = 1
maze[3][0] = 1
maze[4][0] = 1
maze[4][1] = 1
maze[4][2] = 1
maze[4][3] = 1
maze[4][4] = 1
maze[4][5] = 1
maze[4][6] = 1
maze[4][7] = 1
maze[4][8] = 1
maze[4][9] = 1
maze[3][2] = 1

start = (0, 0)
goal = (10, 4)

def draw_maze():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            cell = maze[y][x]
            if cell == 0:
                color = WHITE
            elif cell == 1:
                color = BLACK
            elif cell == 2:
                color = GREEN
            else:
                color = BLUE
            pygame.draw.rect(screen, color, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def draw_path(path):
    for x, y in path:
        maze[y][x] = 2  # Cambia el color de la ruta a verde
        pygame.draw.rect(screen, GREEN, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def bidirectional_a_star():
    open_list_start = [(0, start, [])]
    open_list_goal = [(0, goal, [])]
    heapq.heapify(open_list_start)
    heapq.heapify(open_list_goal)

    path_start = {start: []}
    path_goal = {goal: []}

    optimal_path = []  # Definir optimal_path como una lista vacía

    animation_delay = 0.1  # Velocidad de la animación en segundos

    while open_list_start and open_list_goal:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        time_start, current_start, _ = heapq.heappop(open_list_start)
        if current_start in path_goal:
            intersection_point = current_start
            optimal_path = path_start[current_start] + [intersection_point] + path_goal[intersection_point][::-1]
            break  # Salir del bucle cuando se encuentra la intersección

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            x, y = current_start
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < GRID_WIDTH and 0 <= new_y < GRID_HEIGHT:
                if maze[new_y][new_x] != 1:
                    new_time = time_start + 1
                    new_cost = new_time
                    new_pos = (new_x, new_y)
                    if new_pos not in path_start or new_cost < len(path_start[new_pos]):
                        path_start[new_pos] = path_start[current_start] + [current_start]
                        heapq.heappush(open_list_start, (new_cost, new_pos, []))
                        maze[new_y][new_x] = 2

        time_goal, current_goal, _ = heapq.heappop(open_list_goal)
        if current_goal in path_start:
            intersection_point = current_goal
            optimal_path = path_start[intersection_point] + [intersection_point] + path_goal[current_goal][::-1]
            break  # Salir del bucle cuando se encuentra la intersección

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            x, y = current_goal
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < GRID_WIDTH and 0 <= new_y < GRID_HEIGHT:
                if maze[new_y][new_x] != 1:
                    new_time = time_goal + 1
                    new_cost = new_time
                    new_pos = (new_x, new_y)
                    if new_pos not in path_goal or new_cost < len(path_goal[new_pos]):
                        path_goal[new_pos] = path_goal[current_goal] + [current_goal]
                        heapq.heappush(open_list_goal, (new_cost, new_pos, []))
                        maze[new_y][new_x] = 2

        screen.fill(BLACK)
        draw_maze()

        if optimal_path:
            draw_path(optimal_path)

        pygame.display.flip()

        time.sleep(animation_delay)  # Agregar un retraso de tiempo entre cuadros

    return optimal_path

optimal_path = bidirectional_a_star()

pygame.quit()
sys.exit()
