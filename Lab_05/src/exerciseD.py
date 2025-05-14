from chessPictures import *
from interpreter import draw

# Cuadros base (blanco y negro/negativo)
cuadro_blanco = square
cuadro_negro = square.negative()

#Fila del tablero
fila = cuadro_blanco.join(cuadro_negro).horizontalRepeat(4)

draw(fila)
