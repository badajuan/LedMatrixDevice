"""
Animaciones sobre la matriz de LEDs.
"""
from .matrix import *

def spiral_fill(matrix):
    x, y = 0, 0
    dx, dy = 1, 0
    visited = set()
    matrix.clear()

    for _ in range(8 * 8):
        if 0 <= x < 8 and 0 <= y < 8 and (x, y) not in visited:
            matrix.set_pixel(x, y, 1)
            visited.add((x, y))
            yield  # pause here for next frame
        nx, ny = x + dx, y + dy
        if not (0 <= nx < 8 and 0 <= ny < 8 and (nx, ny) not in visited):
            dx, dy = -dy, dx  # turn right
        x += dx
        y += dy

def blink_actual(matrix,grid,repeats=3):
    for _ in range(repeats):
        matrix.set_grid(grid)
        yield
        matrix.clear()
        yield
    matrix.set_grid(grid)
