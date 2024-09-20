class Pila: #Definición de la pila con sus metodos
    def __init__(self): 
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.empty():
            return self.items.pop()
        return None

    def empty(self):
        return len(self.items) == 0

    def top(self):
        if not self.empty():
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)


class Puzzle4:
    def __init__(self, initial_state, final_state):
        self.initial_state = initial_state
        self.final_state = final_state
        self.moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # derecha, abajo, izquierda, arriba
        self.name_moves = ["Derecha", "Abajo", "Izquierda", "Arriba"]  # Para visualizar los movimientos

    def find_void(self, estado): #Encontrar el espacio vacio (0) 
        for i in range(2):
            for j in range(2):
                if estado[i][j] == 0:
                    return (i, j)
        return None

    def move(self, estado, pos_void, direction): #Mover el espacio vacio 
        x, y = pos_void
        dx, dy = direction
        new_x, new_y = x + dx, y + dy
        
        if 0 <= new_x < 2 and 0 <= new_y < 2:
            new_state = [list(fila) for fila in estado]  # Copia el estado
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            return new_state
        return None

    def its_final_state(self, estado): #Encontrar estado final
        return estado == self.final_state

    def print_state(self, estado): #Imprimir el estado del tablero
        for fila in estado:
            print(fila)
        print()

    def dfs(self):
        stack = Pila()
        stack.push((self.initial_state, []))  # Guardar el estado y el camino
        visited = set()

        while not stack.empty():
            actual_state, path = stack.pop()

            if self.its_final_state(actual_state):
                return path  # Se encontró el estado objetivo

            estado_tuple = tuple(map(tuple, actual_state))  # Convertimos a tupla para poder usar en conjuntos
            if estado_tuple in visited:
                continue

            visited.add(estado_tuple)

            pos_void = self.find_void(actual_state)

            for i, direction in enumerate(self.moves):
                new_state = self.move(actual_state, pos_void, direction)
                if new_state and tuple(map(tuple, new_state)) not in visited:
                    stack.push((new_state, path + [(new_state, self.name_moves[i])]))

        return None  # No se encontró solución

    def show_solution(self, path):
        print("Estado inicial:")
        self.print_state(self.initial_state)
        
        for step, (estado, movimiento) in enumerate(path, 1):
            print(f"Paso {step}: Mover {movimiento}")
            self.print_state(estado)
        
        print("Estado objetivo alcanzado")
initial_state = [
    [1, 2],
    [0, 3]
]

final_state = [
    [1, 2],
    [3, 0]
]

puzzle = Puzzle4(initial_state, final_state)
path = puzzle.dfs()

if path:
    puzzle.show_solution(path)
else:
    print("No se encontró solución")
