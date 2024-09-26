from collections import deque

class Queue: #Cola 
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        return None
    
    def is_empty(self):
        return len(self.queue) == 0

def bfs_maze(maze, start, end): #Algoritmo BFS para resolver el laberinto
    queue = Queue() #Declaración de cola y lista generica. 
    visited = set()
    queue.enqueue((start, [start]))  #(posición actual, ruta recorrida)

    while not queue.is_empty(): #
        (position, path) = queue.dequeue()
        x, y = position

        # Si llegamos a la salida, devolvemos la ruta seguida
        if position == end:
            return path

        # Si ya visitamos esta posición, la ignoramos
        if position in visited:
            continue

        visited.add(position)

        # Movimientos posibles
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for move in moves:
            new_x, new_y = x + move[0], y + move[1]

            # Verificar si no choca con pared y no se sale del laberinto
            if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and maze[new_x][new_y] == 0:
                queue.enqueue(((new_x, new_y), path + [(new_x, new_y)]))

    return None  # Si no se encuentra solución

# Representación del laberinto
maze = [
    [1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1]
]

start = (0, 1)
end = (3, 4)

solution_path = bfs_maze(maze, start, end)

if solution_path:
    print("Camino encontrado:", solution_path)
else:
    print("No hay solución para el laberinto.")
