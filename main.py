import time
import datetime
import copy
import signal
from src.animations import *
from src.matrix import Matrix
from src.display_simulation import MatrixDisplay

m1 = Matrix()
m2 = Matrix()
m3 = Matrix()
m4 = Matrix()
matrices = [m1, m2, m3, m4]
d = MatrixDisplay(matrices)

interrupted = False

def signal_handler(sig, frame):
    global interrupted
    interrupted = True
    print("--Animación interrumpida-- ")

# Registrar el handler para SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, signal_handler)

def animation_spiral(delay=0.2,m=m1):
    global interrupted
    for _ in spiral_fill(m):
        d.update()
        if interrupted: 
            interrupted=False
            break
        time.sleep(delay)

def animation_blink(delay=0.5,m=m1):
    global interrupted
    state = copy.deepcopy(m.get_frame())
    for _ in blink_actual(m, state):
        d.update()
        if interrupted: 
            interrupted=False
            break
        time.sleep(delay)
    d.update()

def animation_counter(delay=0.5,m=m1):
    global interrupted
    for _ in count_numbers(m):
        d.update()
        if interrupted: 
            interrupted=False
            break
        time.sleep(delay)

def animation_alphabet(delay=0.5,m=m1):
    global interrupted
    for _ in count_alphabet(m):
        d.update()
        if interrupted: 
            interrupted=False
            break
        time.sleep(delay)

def animation_characters(delay=0.5,m=m1):
    global interrupted
    for _ in count_characters(m):
        d.update()
        if interrupted: 
            interrupted=False
            break
        time.sleep(delay)

def animation_text(text, delay=0.5):
    """
    Muestra un texto usando las 4 matrices como un solo display.
    """
    byte_rows = string_to_byte_array(text, padding=1)
    matrices_bytes = split_array_to_matrices(byte_rows)
    # Asume que tienes 4 matrices: m1, m2, m3, m4
    for i, m in enumerate([m1, m2, m3, m4]):
        m.set_grid(matrices_bytes[i])
    d.update()
    #time.sleep(delay)

def animation_time(delay=1, loop=False):
    global interrupted
    """
    Muestra la hora y minutos actuales en formato HH:MM usando las 4 matrices como un solo display.
    """
    formats = ["%H:%M", "%H %M"]
    idx = 0
    while True:
        if interrupted:
            interrupted = False
            break
        now = datetime.datetime.now()
        time_str = now.strftime(formats[idx])
        idx = (idx + 1) % 2
        byte_rows = string_to_byte_array(time_str, padding=1, start_padding=1)
        matrices_bytes = split_array_to_matrices(byte_rows)
        for i, m in enumerate([m1, m2, m3, m4]):
            m.set_grid(matrices_bytes[i])
        d.update()
        if not loop:
            break
        for _ in range(5):
            if interrupted:
                interrupted = False
                return
            time.sleep(delay/5)

def animation_timer(minutes, seconds=0, delay=1):
    global interrupted
    """
    Temporizador regresivo MM:SS usando las 4 matrices como un solo display.
    """
    total_seconds = minutes * 60 + seconds
    while total_seconds >= 0:
        if interrupted:
            interrupted = False
            break
        mm = total_seconds // 60
        ss = total_seconds % 60
        time_str = f"{mm:02}:{ss:02}"
        byte_rows = string_to_byte_array(time_str, padding=1, start_padding=1)
        matrices_bytes = split_array_to_matrices(byte_rows)
        for i, m in enumerate([m1, m2, m3, m4]):
            m.set_grid(matrices_bytes[i])
        d.update()
        if total_seconds == 0:
            break
        for _ in range(int(delay * 10)):
            if interrupted:
                interrupted = False
                return
            time.sleep(0.1)
        total_seconds -= 1

def clear_display():
    for m in matrices:
        m.clear()

running = True
while running:
    try:
        text = input("Animación deseada: ").strip().lower()
        match text:
            case "quit":
                running = False
                break
            case "clear":
                clear_display()
            case "fill":
                clear_display()
                animation_spiral()
            case "blink":
                animation_blink()
            case "count":
                clear_display()
                animation_counter()
            case "alphabet":
                clear_display()
                animation_alphabet()
            case "characters":
                clear_display()
                animation_characters()
            case "clock":
                clear_display()
                animation_time(loop=True)
            case "now":
                clear_display()
                animation_time(loop=False)
            case "timer":
                clear_display()
                animation_timer(1,30)
            case "text":
                clear_display()
                animation_text(input("Texto a mostrar: "))
            case "help":
                print("Opciones disponibles:")
                print("  fill        - Animación de llenado en espiral")
                print("  blink       - Parpadeo de la matriz")
                print("  count       - Contador de números")
                print("  alphabet    - Animación de letras")
                print("  characters  - Animación de caracteres especiales")
                print("  clock       - Reloj en tiempo real (loop)")
                print("  now         - Hora actual (una vez)")
                print("  timer       - Temporizador regresivo (1:10)")
                print("  text        - Mostrar texto personalizado")
                print("  clear       - Limpiar todas las matrices")
                print("  quit        - Salir del programa")
                print("  help        - Mostrar este menú de ayuda")
            case _:
                clear_display()
                animation_text(text)
                        
    except Exception as error:
        print("Error: ", error)
        break