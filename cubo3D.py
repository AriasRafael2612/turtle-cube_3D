"""
    Rafael Arias Flores        21760456
    Codigo que dibuja un Cubo 3D usando la libreria Turtle
"""

from turtle import Turtle
from random import random

t = Turtle()

for _ in range(1):
    t.fd(100)  
    t.right(90)  
    t.fd(100)  
    t.right(90) 
    t.fd(100)  
    t.right(90) 
    t.fd(100)  
    
    t.right(45)
    t.fd(100)
    t.right(45)
    t.fd(100)
    t.right(135)
    t.fd(100)
    t.right(-45)
    t.fd(100)

    t.right(-135)
    t.fd(100)
    t.right(-45)
    t.fd(100)

    t.right(180)
    t.fd(100)
    t.right(90)
    t.fd(100)

    t.right(-45)
    t.fd(100)
    t.right(180)
    t.fd(100)

    t.right(-45)
    t.fd(100)
    

input('Parar')
