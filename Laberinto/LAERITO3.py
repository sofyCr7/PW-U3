import pygame
import heapq
import sys

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)  # Cambiar a rojo
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)  # Cambiar a morado


# Definir dimensiones del laberinto
WIDTH, HEIGHT = 220, 100
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Inicializar pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bidirectional A* Maze")

# Crear el laberinto como una matriz
maze = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# Definir paredes
maze[0][0] = 1
maze[0][1] = 1
maze[0][2] = 1
maze[0][3] = 1
maze[0][4] = 1
maze[0][5] = 1
maze[0][6] = 1
maze[0][7] = 1
maze[0][8] = 1
maze[0][9] = 1
maze[0][10] = 1
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
maze[4][10] = 1
maze[1][10] = 1
maze[2][10] = 1
maze[3][10] = 1
maze[2][9] = 1
maze[3][8] = 1
maze[8][3] = 1




# Definir punto de inicio y destino
start = (2, 0)
goal = (8, 4)

# Función para dibujar el laberinto en pantalla
def draw_maze():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            cell = maze[y][x]
            color = WHITE if cell == 0 else BLACK if cell == 1 else BLUE if cell == 2 else RED
            pygame.draw.rect(screen, color, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Función para encontrar la ruta óptima con A* bidireccional
def bidirectional_a_star():
    open_list_start = [(0, start, [])]
    open_list_goal = [(0, goal, [])]
    heapq.heapify(open_list_start)
    heapq.heapify(open_list_goal)
    
    # Rastreo de caminos en ambos sentidos
    path_start = {start: []}
    path_goal = {goal: []}
    
    while open_list_start and open_list_goal:
        # Búsqueda desde el inicio
        time_start, current_start, _ = heapq.heappop(open_list_start)
        if current_start in path_goal:
            intersection_point = current_start
            return path_start[current_start] + [intersection_point] + path_goal[intersection_point][::-1]

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            x, y = current_start
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < GRID_WIDTH and 0 <= new_y < GRID_HEIGHT:
                if maze[new_y][new_x] != 1:
                    new_time = time_start + 1
                    new_cost = new_time  # Puedes ajustar la función de costo según sea necesario
                    new_pos = (new_x, new_y)
                    if new_pos not in path_start or new_cost < len(path_start[new_pos]):
                        path_start[new_pos] = path_start[current_start] + [current_start]
                        heapq.heappush(open_list_start, (new_cost, new_pos, []))
                        maze[new_y][new_x] = 2

        # Búsqueda desde el final
        time_goal, current_goal, _ = heapq.heappop(open_list_goal)
        if current_goal in path_start:
            intersection_point = current_goal
            return path_start[intersection_point] + [intersection_point] + path_goal[current_goal][::-1]

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            x, y = current_goal
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < GRID_WIDTH and 0 <= new_y < GRID_HEIGHT:
                if maze[new_y][new_x] != 1:
                    new_time = time_goal + 1
                    new_cost = new_time  # Puedes ajustar la función de costo según sea necesario
                    new_pos = (new_x, new_y)
                    if new_pos not in path_goal or new_cost < len(path_goal[new_pos]):
                        path_goal[new_pos] = path_goal[current_goal] + [current_goal]
                        heapq.heappush(open_list_goal, (new_cost, new_pos, []))
                        maze[new_y][new_x] = 2

    return None

# Encontrar la ruta óptima
optimal_path = bidirectional_a_star()

# Bucle principal
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    draw_maze()

    # Dibujar la ruta óptima en azul
    if optimal_path:
        for x, y in optimal_path:
            pygame.draw.rect(screen, PURPLE, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))  # Cambiar a morado

    pygame.display.flip()

pygame.quit()
sys.exit()
