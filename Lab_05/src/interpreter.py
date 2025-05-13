import pygame
from pygame.locals import *
from colors import *

def parseLine(DISPLAY, y, s):
    x = 0
    for c in s:
        try:
            pygame.draw.line(DISPLAY, color[c], (x, y), (x, y))
        except KeyError:
            # Si el carácter no está en el diccionario de colores, usar azul por defecto
            pygame.draw.line(DISPLAY, BLUE, (x, y), (x, y))
        x += 1

def draw(picture):
    try:
        # Obtener la imagen del objeto Picture o usar directamente si es una lista
        try:
            img = picture.img
        except AttributeError:
            img = picture

        # Inicializar Pygame
        pygame.init()
        
        # Calcular tamaño de ventana adecuado
        if not img or len(img) == 0:
            raise ValueError("La imagen está vacía")
            
        width = len(img[0]) if len(img) > 0 else 0
        height = len(img)
        
        # Crear ventana (limitamos el tamaño máximo)
        max_size = 800
        cell_size = min(max_size // max(width, height), 10) or 1
        DISPLAY = pygame.display.set_mode((width * cell_size, height * cell_size))
        pygame.display.set_caption("Visualizador de Tablero")

        # Dibujar la imagen
        DISPLAY.fill(BLUE)
        for y, line in enumerate(img):
            for x, char in enumerate(line):
                try:
                    pygame.draw.rect(DISPLAY, color[char], 
                                   (x * cell_size, y * cell_size, cell_size, cell_size))
                except KeyError:
                    pygame.draw.rect(DISPLAY, BLUE, 
                                   (x * cell_size, y * cell_size, cell_size, cell_size))

        # Bucle principal mejorado
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
            
            pygame.display.update()

    except Exception as e:
        print(f"Error: {e}")
    finally:
        pygame.quit()