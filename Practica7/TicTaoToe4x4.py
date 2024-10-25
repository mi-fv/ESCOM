import math
from typing import List, Tuple, Optional

class Gato4x4:
    def __init__(self):
        self.tablero = [' ' for _ in range(16)]
        self.jugador_actual = 'X'

    def hacer_movimiento(self, posicion: int) -> bool:
        if self.tablero[posicion] == ' ':
            self.tablero[posicion] = self.jugador_actual
            self.jugador_actual = 'O' if self.jugador_actual == 'X' else 'X'
            return True
        return False

    def obtener_movimientos_validos(self) -> List[int]:
        return [i for i, casilla in enumerate(self.tablero) if casilla == ' ']

    def verificar_ganador(self) -> Optional[str]:
        # Verificar filas y columnas
        for i in range(4):
            if self.tablero[i*4] == self.tablero[i*4+1] == self.tablero[i*4+2] == self.tablero[i*4+3] != ' ':
                return self.tablero[i*4]
            if self.tablero[i] == self.tablero[i+4] == self.tablero[i+8] == self.tablero[i+12] != ' ':
                return self.tablero[i]
        
        # Verificar diagonales
        if self.tablero[0] == self.tablero[5] == self.tablero[10] == self.tablero[15] != ' ':
            return self.tablero[0]
        if self.tablero[3] == self.tablero[6] == self.tablero[9] == self.tablero[12] != ' ':
            return self.tablero[3]
        
        if ' ' not in self.tablero:
            return 'Empate'
        
        return None

    def imprimir_tablero(self):
        for i in range(4):
            print('|'.join(self.tablero[i*4:(i+1)*4]))
            if i < 3:
                print('-' * 7)

def minimax(estado: Gato4x4, profundidad: int, alpha: float, beta: float, es_maximizador: bool) -> Tuple[int, float]:
    ganador = estado.verificar_ganador()
    if ganador == 'X':
        return None, 1
    elif ganador == 'O':
        return None, -1
    elif ganador == 'Empate':
        return None, 0
    
    if profundidad == 0:
        return None, 0
    
    if es_maximizador:
        mejor_valor = -math.inf
        mejor_movimiento = None
        for movimiento in estado.obtener_movimientos_validos():
            nuevo_estado = Gato4x4()
            nuevo_estado.tablero = estado.tablero.copy()
            nuevo_estado.jugador_actual = estado.jugador_actual
            nuevo_estado.hacer_movimiento(movimiento)
            _, valor = minimax(nuevo_estado, profundidad - 1, alpha, beta, False)
            if valor > mejor_valor:
                mejor_valor = valor
                mejor_movimiento = movimiento
            alpha = max(alpha, mejor_valor)
            if beta <= alpha:
                break
        return mejor_movimiento, mejor_valor
    else:
        mejor_valor = math.inf
        mejor_movimiento = None
        for movimiento in estado.obtener_movimientos_validos():
            nuevo_estado = Gato4x4()
            nuevo_estado.tablero = estado.tablero.copy()
            nuevo_estado.jugador_actual = estado.jugador_actual
            nuevo_estado.hacer_movimiento(movimiento)
            _, valor = minimax(nuevo_estado, profundidad - 1, alpha, beta, True)
            if valor < mejor_valor:
                mejor_valor = valor
                mejor_movimiento = movimiento
            beta = min(beta, mejor_valor)
            if beta <= alpha:
                break
        return mejor_movimiento, mejor_valor

def jugar_humano_vs_humano():
    juego = Gato4x4()
    while True:
        juego.imprimir_tablero()
        print(f"Turno del jugador {juego.jugador_actual}")
        movimiento = int(input("Ingrese la posición (0-15): "))
        if juego.hacer_movimiento(movimiento):
            ganador = juego.verificar_ganador()
            if ganador:
                juego.imprimir_tablero()
                if ganador == 'Empate':
                    print("¡Es un empate!")
                else:
                    print(f"¡El jugador {ganador} ha ganado!")
                break
        else:
            print("Movimiento inválido, intente de nuevo.")

def jugar_humano_vs_ia():
    juego = Gato4x4()
    while True:
        juego.imprimir_tablero()
        if juego.jugador_actual == 'X':
            print("Turno del jugador humano (X)")
            movimiento = int(input("Ingrese la posición (0-15): "))
            if not juego.hacer_movimiento(movimiento):
                print("Movimiento inválido, intente de nuevo.")
                continue
        else:
            print("Turno de la IA (O)")
            movimiento, _ = minimax(juego, 5, -math.inf, math.inf, False)
            juego.hacer_movimiento(movimiento)
        
        ganador = juego.verificar_ganador()
        if ganador:
            juego.imprimir_tablero()
            if ganador == 'Empate':
                print("¡Es un empate!")
            else:
                print(f"¡El jugador {ganador} ha ganado!")
            break

def jugar_ia_vs_ia():
    juego = Gato4x4()
    while True:
        juego.imprimir_tablero()
        print(f"Turno de la IA ({juego.jugador_actual})")
        movimiento, _ = minimax(juego, 5, -math.inf, math.inf, juego.jugador_actual == 'X')
        juego.hacer_movimiento(movimiento)
        
        ganador = juego.verificar_ganador()
        if ganador:
            juego.imprimir_tablero()
            if ganador == 'Empate':
                print("¡Es un empate!")
            else:
                print(f"¡La IA {ganador} ha ganado!")
            break

def main():
    print("Bienvenido al juego del Gato 4x4")
    print("1. Humano vs Humano")
    print("2. Humano vs IA")
    print("3. IA vs IA")
    opcion = int(input("Seleccione el modo de juego: "))
    
    if opcion == 1:
        jugar_humano_vs_humano()
    elif opcion == 2:
        jugar_humano_vs_ia()
    elif opcion == 3:
        jugar_ia_vs_ia()
    else:
        print("Opción inválida")

if __name__ == "__main__":
    main()