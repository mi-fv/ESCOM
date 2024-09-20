class Laberinto: #Declaración de metodo con constructor 
    def __init__(self, maze, start, exit):
        self.maze = maze
        self.n = len(maze)
        self.start = start
        self.exit = exit
        self.moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # derecha, abajo, izquierda, arriba
        self.path = []

    def valid_position(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.n and self.maze[x][y] == 0

    def dfs(self, x, y):
        if (x, y) == self.exit:
            self.path.append((x, y))
            return True #Encuentra salida

        # Marcar la posición actual como parte del camino.
        self.maze[x][y] = 2  # Marcamos con el número para evitar volver a pasar.
        self.path.append((x, y))
        self.show_maze()

        for move in self.moves:
            new_x, new_y = x + move[0], y + move[1]
            if self.valid_position(new_x, new_y):
                if self.dfs(new_x, new_y):
                    return True  # Movimientos hasta encontrar salida

        # Backtracking
        self.path.pop()
        self.maze[x][y] = 0  # Desmarcamos el camino
        self.show_maze()
        return False

    def resolve(self): #Resolver desde posicion de inicio 
        x_initial, y_initial = self.start
        if not self.dfs(x_initial, y_initial):
            print("No se encontró un camino a la salida")
        else:
            print("Se encontró un camino a la salida")
            print("Camino recorrido:", self.path)

    def show_maze(self):
        print("Laberinto:")
        for fila in self.maze:
            print(fila)
        print()


# Definición del laberinto (1 representa pared, 0 representa camino)
maze = [
    [1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1]
]
start = (0, 1)  
exit = (3, 4)   

Maze_example = Laberinto(maze, start, exit)
Maze_example.resolve()
