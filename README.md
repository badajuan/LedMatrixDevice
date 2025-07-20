# LEDMatrixSimulation

Simulación de una matriz de LEDs 8x8 con animaciones y visualización en Tkinter.

## Estructura del proyecto

- `src/` - Código fuente principal
- `README.md` - Información del proyecto

## Uso

Ejecuta `main.py` para iniciar la simulación.  
Al iniciar, escribe el nombre de la animación que deseas ejecutar y presiona Enter.

### Opciones disponibles en el menú principal

- `fill`        - Animación de llenado en espiral de la matriz 1
- `blink`       - Parpadeo de la matriz
- `count`       - Contador de números
- `alphabet`    - Animación de letras
- `characters`  - Animación de caracteres especiales
- `clock`       - Reloj en tiempo real (loop)
- `now`         - Hora actual (una vez)
- `timer`       - Temporizador regresivo (1:10)
- `text`        - Mostrar texto personalizado (te pedirá el texto)
- `clear`       - Limpiar todas las matrices
- `quit`        - Salir del programa
- `help`        - Mostrar este menú de ayuda

Puedes interrumpir cualquier animación en curso presionando `Ctrl+C` para volver al menú principal.

## Requisitos

- Python 3.x
- Tkinter

## Licencia