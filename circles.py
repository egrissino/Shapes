## Evan Grissino
## 01/07/17
## Shapes with Turtle
## Python 2.x only

from turtle import *
from random import *

def Circle(x, y, r, N = 20):
    penup()
    goto(x, y + r)
    setheading(0)
    pendown()

    C = 2 * pi * r

    for _ in range(N):
        rt(360 / N)
        forward(C / N)

def mandala():
    D = 50
    for R in range(D, 500, D):
        for t in range(44):
            x = R * cos(t)
            y = R * sin(t)
            Circle(x, y, D/2 + 10)

def polygon(x, y, N, r = 10, theta = 90):
    R = float(r) / 2.0 / sin(pi / N)
    
    penup()
    goto(x, y)
    setheading(theta)
    forward(R)
    rt(90)
    lt(180.0 / float(N))
    pendown()

    
    for _ in range(N):
        rt(360.0 / float(N))
        forward(r)
    

def pent_a_port():
    for R in range(1, 35, 5):
        for angle in range(0, 360, 60):
            polygon(0, 0, 5, R**1.7 , angle)

    for angle in range(0, 360, 12):
        penup()
        goto(0, 0)
        setheading(angle)
        pendown()
        forward(1000)

def random():
    r = randint(30, 200)
    x = randint(-300, 300)
    y = randint(-300, 300)
    N = randint(3, 8)
    theta = randint(0, 360)

    polygon(0, 0, N, r, 0)

def main():
    mandala()
    



setup()
speed(0)
ht() 
main()
mainloop()
