"""
Clase principal para manejar una matriz de LEDs o píxeles.
"""
class Matrix:
    def __init__(self, rows=8, cols=8):
        self.rows = rows
        self.cols = cols
        # Inicializa la matriz con ceros
        self.clear()

    # Limpia la matriz con todos los valores en 0.
    def clear(self):
        self.grid = [[0]*self.cols for _ in range(self.rows)]

    # Establece el valor de un píxel específico.
    def set_pixel(self, x, y, value):
        if 0 <= x < self.cols and 0 <= y < self.rows:
            self.grid[y][x] = value
    
    # Reemplaza toda la matriz si el tamaño es correcto.
    def set_grid(self, new_grid):
        if len(new_grid) == self.rows and all(len(row) == self.cols for row in new_grid):
            self.grid = [row[:] for row in new_grid]

    # Devuelve el estado actual de la matriz.
    def get_frame(self):
        return self.grid
