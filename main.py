import time
import copy
from src.animations import *
from src.matrix import Matrix
from src.display_simulation import MatrixDisplay

m1 = Matrix()
m2 = Matrix()
matrices = [m1, m2]
d = MatrixDisplay(matrices)

def animation_spiral(delay=0.2,m=m1):
    for _ in spiral_fill(m):
        d.update()
        time.sleep(delay)

def animation_blink(delay=0.5,m=m1):
    state = copy.deepcopy(m.get_frame())
    for _ in blink_actual(m, state):
        d.update()
        time.sleep(delay)
    d.update()

running = True
while running:
    try:
        text = input("Animación deseada: ").strip().lower()
        match text:
            case "quit":
                running = False
                break
            case "fill":
                m1.clear()
                animation_spiral()
            case "blink":
                animation_blink()
            case _:
                print("  Animación desconocida")
    except Exception as error:
        print("Error: ", error)
        break