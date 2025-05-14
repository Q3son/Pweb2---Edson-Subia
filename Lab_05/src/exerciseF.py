from chessPictures import *
from interpreter import draw

# Cuadros base (blanco y negro/negativo)
cuadro_blanco = square
cuadro_negro = square.negative()

# Filas del tablero
fila_superior = cuadro_blanco.join(cuadro_negro).horizontalRepeat(4)
fila_inferior = cuadro_blanco.join(cuadro_negro).horizontalRepeat(4).negative()

# Tablero (4 filas en total)
tablero = fila_inferior.under(fila_superior).verticalRepeat(2)
draw(tablero)
