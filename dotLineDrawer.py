"""
    Rafael Arias Flores - 21760456
    Funcion para hacer lineas cual solo utilizara la funcion de dibujar punto
"""


import turtle as t
import time

def interpolate(start, d0, end, d1):
    """Genera valores intermedios entre dos puntos"""
    if start == end:
        return [d0] * (end - start + 1)

    step = (d1 - d0) / (end - start)
    return [d0 + i * step for i in range(end - start + 1)]

def draw_dot(x, y, size):
    """Dibuja un punto en la posición dada"""
    t.penup()
    t.goto(x, y)
    t.dot(size)

def draw_custom_line(point1, point2, size=3):
    """Dibuja una línea usando solo puntos con interpolación"""
    x1, y1 = point1
    x2, y2 = point2

    if abs(x2 - x1) > abs(y2 - y1):
        if x1 > x2:
            x1, y1, x2, y2 = x2, y2, x1, y1
        y_values = interpolate(x1, y1, x2, y2)
        for i, x in enumerate(range(x1, x2 + 1)):
            draw_dot(x, round(y_values[i]), size)
    else:
        if y1 > y2:
            x1, y1, x2, y2 = x2, y2, x1, y1
        x_values = interpolate(y1, x1, y2, x2)
        for i, y in enumerate(range(y1, y2 + 1)):
            draw_dot(round(x_values[i]), y, size)

if __name__ == "__main__":
    t.speed(0)  

  #  t.bgcolor("black")  # Es para cambiar el color el Fondo
  #  t.pencolor("cyan")  # Cambia el color de los puntos

  
    puntos = [
            (0, 0), (100, 100),
            (100, 100), (200, 0),
            (200, 0), (0, 0),
            ]
            
    for i in range(0, len(puntos), 2):
        draw_custom_line(puntos[i], puntos[i + 1], 3)

    t.hideturtle()
    time.sleep(5)
