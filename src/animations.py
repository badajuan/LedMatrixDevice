"""
Animaciones sobre la matriz de LEDs.
"""
from .matrix import *

# Definiciones de imágenes de números 0-9 como arrays de bytes (cada entero representa una fila)
NUM_IMAGES = [
    [0b000000, 0b011110, 0b110011, 0b110111, 0b111011, 0b110011, 0b110011, 0b011110],
    [0b000000, 0b001100, 0b001100, 0b011100, 0b001100, 0b001100, 0b001100, 0b111111],
    [0b000000, 0b011110, 0b110011, 0b000011, 0b000110, 0b011000, 0b110000, 0b111111],
    [0b000000, 0b011110, 0b110011, 0b000011, 0b001110, 0b000011, 0b110011, 0b011110],
    [0b000000, 0b000110, 0b001110, 0b010110, 0b100110, 0b111111, 0b000110, 0b000110],
    [0b000000, 0b111111, 0b110000, 0b111110, 0b000011, 0b000011, 0b110011, 0b011110],
    [0b000000, 0b011110, 0b110011, 0b110000, 0b111110, 0b110011, 0b110011, 0b011110],
    [0b000000, 0b111111, 0b110011, 0b000110, 0b000110, 0b001100, 0b001100, 0b001100],
    [0b000000, 0b011110, 0b110011, 0b110011, 0b011110, 0b110011, 0b110011, 0b011110],
    [0b000000, 0b011110, 0b110011, 0b110011, 0b011111, 0b000011, 0b110011, 0b011110],
]
NUM_IMAGES_LEN = len(NUM_IMAGES)

# Definiciones de letras A-Z en mayusculas y minusculas
LET_IMAGES = [
    [0b000000, 0b011110, 0b110011, 0b110011, 0b111111, 0b110011, 0b110011, 0b110011],
    [0b000000, 0b111110, 0b110011, 0b110011, 0b111110, 0b110011, 0b110011, 0b111110],
    [0b000000, 0b011110, 0b110011, 0b110000, 0b110000, 0b110000, 0b110011, 0b011110],
    [0b000000, 0b111110, 0b110011, 0b110011, 0b110011, 0b110011, 0b110011, 0b111110],
    [0b000000, 0b111111, 0b110000, 0b110000, 0b111110, 0b110000, 0b110000, 0b111111],
    [0b000000, 0b111111, 0b110000, 0b110000, 0b111110, 0b110000, 0b110000, 0b110000],
    [0b000000, 0b011110, 0b110011, 0b110000, 0b110000, 0b110111, 0b110011, 0b011110],
    [0b000000, 0b110011, 0b110011, 0b110011, 0b111111, 0b110011, 0b110011, 0b110011],
    [0b000000, 0b011110, 0b001100, 0b001100, 0b001100, 0b001100, 0b001100, 0b011110],
    [0b000000, 0b001111, 0b000110, 0b000110, 0b000110, 0b110110, 0b110110, 0b011100],
    [0b000000, 0b110011, 0b110110, 0b111100, 0b111000, 0b111100, 0b110110, 0b110011],
    [0b000000, 0b110000, 0b110000, 0b110000, 0b110000, 0b110000, 0b110000, 0b111111],
    [0b000000, 0b110001, 0b111011, 0b111111, 0b110101, 0b110001, 0b110001, 0b110001],
    [0b000000, 0b110001, 0b111001, 0b111101, 0b110111, 0b110011, 0b110001, 0b110001],
    [0b000000, 0b011110, 0b110011, 0b110011, 0b110011, 0b110011, 0b110011, 0b011110],
    [0b000000, 0b111110, 0b110011, 0b110011, 0b110011, 0b111110, 0b110000, 0b110000],
    [0b000000, 0b011110, 0b110011, 0b110011, 0b110011, 0b110111, 0b011110, 0b000011],
    [0b000000, 0b111110, 0b110011, 0b110011, 0b111110, 0b111100, 0b110110, 0b110011],
    [0b000000, 0b011110, 0b110011, 0b110000, 0b011110, 0b000011, 0b110011, 0b011110],
    [0b000000, 0b111111, 0b101101, 0b001100, 0b001100, 0b001100, 0b001100, 0b001100],
    [0b000000, 0b110011, 0b110011, 0b110011, 0b110011, 0b110011, 0b110011, 0b011111],
    [0b000000, 0b110011, 0b110011, 0b110011, 0b110011, 0b110011, 0b011110, 0b001100],
    [0b000000, 0b110001, 0b110001, 0b110001, 0b110101, 0b111111, 0b111011, 0b110001],
    [0b000000, 0b110001, 0b110001, 0b011011, 0b001110, 0b011011, 0b110001, 0b110001],
    [0b000000, 0b110011, 0b110011, 0b110011, 0b011110, 0b001100, 0b001100, 0b001100],
    [0b000000, 0b111111, 0b000011, 0b000110, 0b001100, 0b011000, 0b110000, 0b111111],
    [0b000000, 0b000000, 0b000000, 0b011110, 0b000011, 0b011111, 0b110011, 0b011111],
    [0b000000, 0b110000, 0b110000, 0b110000, 0b111110, 0b110011, 0b110011, 0b111110],
    [0b000000, 0b000000, 0b000000, 0b011110, 0b110011, 0b110000, 0b110011, 0b011110],
    [0b000000, 0b000011, 0b000011, 0b000011, 0b011111, 0b110011, 0b110011, 0b011111],
    [0b000000, 0b000000, 0b000000, 0b011110, 0b110011, 0b111111, 0b110000, 0b011110],
    [0b000000, 0b001110, 0b011011, 0b011000, 0b011000, 0b111110, 0b011000, 0b011000],
    [0b000000, 0b000000, 0b011111, 0b110011, 0b110011, 0b011111, 0b000011, 0b011110],
    [0b000000, 0b110000, 0b110000, 0b110000, 0b111110, 0b110011, 0b110011, 0b110011],
    [0b000000, 0b000000, 0b001100, 0b000000, 0b001100, 0b001100, 0b001100, 0b011110],
    [0b000000, 0b000110, 0b000000, 0b000110, 0b000110, 0b110110, 0b110110, 0b011100],
    [0b000000, 0b110000, 0b110000, 0b110011, 0b110110, 0b111100, 0b110110, 0b110011],
    [0b000000, 0b001100, 0b001100, 0b001100, 0b001100, 0b001100, 0b001100, 0b001100],
    [0b000000, 0b000000, 0b000000, 0b110001, 0b111011, 0b111111, 0b110101, 0b110101],
    [0b000000, 0b000000, 0b000000, 0b111110, 0b111111, 0b110011, 0b110011, 0b110011],
    [0b000000, 0b000000, 0b000000, 0b011110, 0b110011, 0b110011, 0b110011, 0b011110],
    [0b000000, 0b000000, 0b111110, 0b110011, 0b110011, 0b111110, 0b110000, 0b110000],
    [0b000000, 0b000000, 0b011110, 0b110110, 0b110110, 0b011110, 0b000110, 0b000111],
    [0b000000, 0b000000, 0b000000, 0b111110, 0b110011, 0b110011, 0b110000, 0b110000],
    [0b000000, 0b000000, 0b000000, 0b011111, 0b100000, 0b011110, 0b000001, 0b111110],
    [0b000000, 0b000000, 0b001100, 0b001100, 0b111111, 0b001100, 0b001100, 0b001100],
    [0b000000, 0b000000, 0b000000, 0b110011, 0b110011, 0b110011, 0b110011, 0b011111],
    [0b000000, 0b000000, 0b000000, 0b000000, 0b110011, 0b110011, 0b011110, 0b001100],
    [0b000000, 0b000000, 0b000000, 0b110001, 0b110101, 0b110101, 0b110101, 0b011111],
    [0b000000, 0b000000, 0b000000, 0b110011, 0b011110, 0b001100, 0b011110, 0b110011],
    [0b000000, 0b000000, 0b000000, 0b110011, 0b110011, 0b011111, 0b000011, 0b011110],
    [0b000000, 0b000000, 0b000000, 0b011110, 0b000110, 0b001100, 0b011000, 0b011110],
]
LET_IMAGES_LEN = len(LET_IMAGES)

# The only char defined is ':'
CHAR_IMAGES = [
    [0b00,0b00,0b11,0b11,0b00,0b11,0b11,0b00]
]
CHAR_IMAGES_LEN = len(CHAR_IMAGES)

# Mapeo de letras, números y caracteres especiales a sus imágenes
ALL_CHARS = (
    [chr(i) for i in range(ord('A'), ord('Z') + 1)] +
    [chr(i) for i in range(ord('a'), ord('z') + 1)] +
    [str(i) for i in range(10)] +
    [':']  # Puedes agregar más caracteres aquí si defines sus imágenes
)
ALL_IMAGES = LET_IMAGES + NUM_IMAGES + CHAR_IMAGES
CHAR_IMAGE_MAP = dict(zip(ALL_CHARS, ALL_IMAGES))

# Definir el ancho de cada carácter en el mismo orden que ALL_CHARS
ALL_WIDTHS = (
    [6]*len(LET_IMAGES) +    # Letras: 6 bits de ancho
    [6]*len(NUM_IMAGES) +    # Números: 6 bits de ancho
    [2]*len(CHAR_IMAGES)     # ':' por ejemplo, 2 bits de ancho
)
CHAR_WIDTH_MAP = dict(zip(ALL_CHARS, ALL_WIDTHS))

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

def count_numbers(matrix):
    """
    Animación que cuenta del 0 al 9 mostrando cada número en la matriz.
    """
    for num in range(NUM_IMAGES_LEN):
        # Desplazar cada fila 1 bit a la derecha
        shifted_image = [row << 1 for row in NUM_IMAGES[num]]
        matrix.set_grid(shifted_image)
        yield

def count_alphabet(matrix):
    for let in range(LET_IMAGES_LEN):
        shifted_image = [row << 1 for row in LET_IMAGES[let]]
        matrix.set_grid(shifted_image)
        yield

def count_characters(matrix):
    for char in range(CHAR_IMAGES_LEN):
        shifted_image = [row << 3 for row in CHAR_IMAGES[char]]
        matrix.set_grid(shifted_image)
        yield

def string_to_byte_array(text, padding=1, start_padding=1):
    """
    Convierte un string en un array de filas, usando el ancho real de cada carácter según su definición.
    Los espacios se interpretan como 3 columnas de padding.
    """
    result = [[] for _ in range(8)]
    # Padding inicial
    for row_idx in range(8):
        result[row_idx].extend([0]*start_padding)
    for char in text:
        if char == ' ':
            for row_idx in range(8):
                result[row_idx].extend([0]*3)  # Espacio = 3 columnas apagadas
        else:
            image = CHAR_IMAGE_MAP.get(char, [0]*8)
            width = CHAR_WIDTH_MAP.get(char, 6)
            for row_idx in range(8):
                row_val = image[row_idx] if row_idx < len(image) else 0
                bits = [(row_val >> (width-1-i)) & 1 for i in range(width)]
                result[row_idx].extend(bits)
                result[row_idx].extend([0]*padding)
    return result

def split_array_to_matrices(big_array):
    """
    Divide big_array (lista de 8 listas de hasta 32 bytes) en 4 matrices de 8x8 alineando a la izquierda.
    Si hay más de 32 columnas, descarta el resto. Si hay menos, rellena con ceros.
    """
    matrices = []
    for m in range(4):
        matrix = []
        for row in big_array:
            # Extrae los 8 bytes correspondientes a la matriz actual
            start = m * 8
            end = start + 8
            # Si la fila es más corta, rellena con ceros
            segment = row[start:end] + [0] * (8 - len(row[start:end]))
            matrix.append(segment)
        # Si hay menos de 8 filas, rellena con filas apagadas
        while len(matrix) < 8:
            matrix.append([0]*8)
        # Convierte cada fila de 8 bits a un byte
        matrix_bytes = []
        for bits in matrix[:8]:
            byte = 0
            for bit in bits:
                byte = (byte << 1) | bit
            matrix_bytes.append(byte)
        matrices.append(matrix_bytes)
    return matrices
