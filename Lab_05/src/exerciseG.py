from chessPictures import *
from interpreter import draw

def place_piece(piece, square_img):
    """Coloca una pieza centrada en un cuadro"""
    piece_img = piece.img
    background = [list(row) for row in square_img.img]  # Convertir a lista mutable
    
    # Calcular posición de inicio para centrar
    start_y = (len(background) - len(piece_img)) // 2
    start_x = (len(background[0]) - len(piece_img[0])) // 2
    
    # Superponer la pieza
    for y in range(len(piece_img)):
        for x in range(len(piece_img[y])):
            if piece_img[y][x].strip():  # Si no es espacio vacío
                background[y + start_y][x + start_x] = piece_img[y][x]
    
    # Convertir de vuelta a strings
    combined = [''.join(row) for row in background]
    return Picture(combined)

def create_piece_row(pieces, is_white_row):
    """Crea una fila de piezas sobre cuadros alternados"""
    row_pictures = []
    for i, piece in enumerate(pieces):
        square_color = square if (i + is_white_row) % 2 == 0 else square.negative()
        placed_piece = place_piece(piece, square_color)
        row_pictures.append(placed_piece)
    
    # Unir progresivamente las imágenes
    result = row_pictures[0]
    for pic in row_pictures[1:]:
        result = result.join(pic)
    return result

# Configuración de piezas
black_pieces = [rock, knight, bishop, queen, king, bishop, knight, rock]
white_pieces = [rock, knight, bishop, queen, king, bishop, knight, rock]

# Construir filas
first_row = create_piece_row([p.negative() for p in black_pieces], False)
second_row = create_piece_row([pawn.negative()]*8, True)
seventh_row = create_piece_row([pawn]*8, False)
eighth_row = create_piece_row(white_pieces, True)

# Tablero central vacío
empty_pair = square.join(square.negative()).horizontalRepeat(4)
center_board = empty_pair.up(empty_pair.negative()).verticalRepeat(2)

# Ensamblar tablero completo
chessboard = (
    first_row
    .up(second_row)
    .up(center_board)
    .up(seventh_row)
    .up(eighth_row)
)

draw(chessboard)