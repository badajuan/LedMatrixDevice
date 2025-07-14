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
        # Si es una lista de filas (listas de 0/1)
        if len(new_grid) == self.rows and all(isinstance(row, list) and len(row) == self.cols for row in new_grid):
            self.grid = [row[:] for row in new_grid]
        # Si es una lista de bytes/enteros (cada uno representa una fila)
        elif len(new_grid) == self.rows and all(isinstance(row, (int, bytes)) for row in new_grid):
            self.grid = [self._byte_to_row(row) for row in new_grid]
        else:
            raise ValueError("Formato de grid no válido para set_grid")

    def _byte_to_row(self, value):
        # Convierte un entero (byte) en una lista de bits de longitud self.cols
        if isinstance(value, bytes):
            value = int.from_bytes(value, 'big')
        return [(value >> (self.cols - 1 - i)) & 1 for i in range(self.cols)]

    # Devuelve el estado actual de la matriz.
    def get_frame(self):
        return self.grid
