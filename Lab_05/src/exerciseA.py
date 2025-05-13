from chessPictures import *
from interpreter import draw

# Caballos base (blanco y negativo/negro)
caballo_blanco = knight
caballo_negro = knight.negative()

# Fila superior: blanco + negro
fila_superior = caballo_blanco.join(caballo_negro)
# Fila inferior: negro + blanco
fila_inferior = caballo_negro.join(caballo_blanco)

# Combinar ambas filas para mostrar 4 caballos
tablero_final = fila_superior.up(fila_inferior)

# Mostrar resultado
draw(tablero_final)