from colors import *

class Picture:
    def __init__(self, img):
        self.img = img

    def __eq__(self, other):
        return self.img == other.img

    def _invColor(self, color):
        return inverter.get(color, color)  # Usando .get() como condicional implícito

    def verticalMirror(self):
        """Espejo vertical: invierte cada fila"""
        return Picture([row[::-1] for row in self.img])  # Lista por comprensión

    def horizontalMirror(self):
        """Espejo horizontal: invierte el orden de las filas"""
        return Picture(self.img[::-1])  # Slicing permitido

    def negative(self):
        """Negativo: aplica _invColor a cada carácter"""
        return Picture([
            ''.join([self._invColor(c) for c in row])  # join + lista por comprensión
            for row in self.img
        ])

    def join(self, p):
        """Une horizontalmente: self + p"""
        return Picture([
            self.img[i] + p.img[i]  # Concatenación (+) con range
            for i in range(len(self.img))
        ])

    def up(self, p):
        """Une verticalmente: self arriba de p"""
        return Picture(self.img + p.img)  # Concatenación de listas (+)

    def under(self, p):
        """Une verticalmente: p arriba de self"""
        return Picture(p.img + self.img)  # Concatenación de listas (+)

    def horizontalRepeat(self, n):
        """Repite la imagen horizontalmente n veces"""
        return Picture([
            row * n  # Uso de * para strings (equivalente a join)
            for row in self.img
        ])

    def verticalRepeat(self, n):
        """Repite la imagen verticalmente n veces"""
        return Picture(self.img * n)  # Uso de * para listas
    
    def overlay(self, background):
        """Superpone esta imagen (pieza) sobre un fondo (cuadro).
        La pieza reemplazará los espacios vacíos (' ') del fondo."""
        # Verificar que las imágenes tienen el mismo tamaño
        if len(self.img) != len(background.img) or len(self.img[0]) != len(background.img[0]):
            raise ValueError("Las imágenes deben tener las mismas dimensiones")
        
        combined = []
        for piece_row, bg_row in zip(self.img, background.img):
            combined_row = ""
            for piece_char, bg_char in zip(piece_row, bg_row):
                # Mantener el carácter de la pieza si no es espacio vacío, sino usar el fondo
                combined_row += piece_char if piece_char.strip() else bg_char
            combined.append(combined_row)
        return Picture(combined)