"""
Simulación de la matriz led en pantalla con un solo canvas y múltiples matrices 8x8.
"""
import tkinter as tk
import sys

# Cuando la ventana de tk es cerrada, cierra el programa principal que lo ejecutó
def on_closing():
    print("\n---VENTANA CERRADA---")
    sys.exit()

class MatrixDisplay:
    def __init__(self, matrices, size=40):
        self.matrices = matrices  # lista de objetos Matrix
        self.matrices_count = len(matrices)
        self.size = size
        self.rows = 8
        self.cols = 8
        self.window = tk.Tk()
        self.canvas = tk.Canvas(
            self.window,
            width=self.cols * size * self.matrices_count + (self.matrices_count - 1),
            height=self.rows * size,
            bg='gray10'  # fondo negro
        )
        self.canvas.pack()
        self.rects = [
            [[None]*self.cols for _ in range(self.rows)]
            for _ in range(self.matrices_count)
        ]
        self._draw_grids()
        self.window.protocol("WM_DELETE_WINDOW", on_closing)

    def _draw_grids(self):
        for m in range(self.matrices_count):
            offset_x = m * self.cols * self.size + m  # +m para separar 1px entre matrices
            for y in range(self.rows):
                for x in range(self.cols):
                    self.rects[m][y][x] = self.canvas.create_oval(
                        offset_x + x*self.size, y*self.size,
                        offset_x + (x+1)*self.size, (y+1)*self.size,
                        fill='black', outline='gray15'
                    )
            # Línea divisoria (más visible)
            if m < self.matrices_count - 1:
                line_x = offset_x + self.cols * self.size
                self.canvas.create_line(line_x, 0, line_x, self.rows * self.size, fill="gray30", width=2)

    def update(self):
        for m, matrix in enumerate(self.matrices):
            frame = matrix.get_frame()
            for y in range(self.rows):
                for x in range(self.cols):
                    color = 'red' if frame[y][x] else 'black'
                    self.canvas.itemconfig(self.rects[m][y][x], fill=color)
        self.window.update_idletasks()
        self.window.update()
