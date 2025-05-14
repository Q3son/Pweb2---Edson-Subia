from chessPictures import *
from interpreter import draw

# Reina base (blanco)
Reina_blanca = queen

# Fila Reinas (x4)
fila = queen.horizontalRepeat(4)

# Mostrar Tablero
tablero_final = fila
draw(tablero_final)