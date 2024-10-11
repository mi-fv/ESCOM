import numpy as np

def himmelblau(x, y):
    """
    Calcula el valor de la función de Himmelblau para un par (x, y).
    """
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2

def find_minima_random_search(iterations=10000):
    """
    Encuentra los mínimos de la función de Himmelblau mediante búsqueda aleatoria.
    
    Parameters:
    - iterations: Número de puntos aleatorios a evaluar.
    
    Returns:
    - Lista de los mejores 4 mínimos encontrados.
    """
    # Listas para almacenar los mejores valores de (x, y) y sus correspondientes f(x, y)
    best_points = []
    
    # Generar puntos aleatorios y evaluar la función
    for _ in range(iterations):
        # Generar x y y aleatorios dentro de [-5, 5]
        x = np.random.uniform(-5, 5)
        y = np.random.uniform(-5, 5)
        
        # Evaluar la función de Himmelblau
        f_val = himmelblau(x, y)
        
        # Almacenar los resultados
        best_points.append((x, y, f_val))
    
    # Ordenar los puntos según el valor de f(x, y)
    best_points.sort(key=lambda point: point[2])
    
    # Tomar los 4 mejores
    top_4 = best_points[:4]
    
    return top_4

def main():
    top_4_minima = find_minima_random_search()
    
    print("Los mejores 4 valores donde la función es mínima:")
    for i, (x, y, f_val) in enumerate(top_4_minima, 1):
        print(f"{i}: x = {x:.6f}, y = {y:.6f}, f(x,y) = {f_val:.6f}")

if __name__ == "__main__":
    main()
