import random
from turtle import *
pencolor('red')
pensize(1)
bgcolor('black')
fillcolor('yellow')

angle = 0
rainbow =["red", "orange", "yellow", "green", "blue", "purple"]
bow = 0
rain=bow%6
side = 200
number=1
while number < 100:
    begin_fill()# hash out beginfill and endfill for unfilled polygons
    fillcolor(rainbow[rain])
    pencolor(rainbow[rain])
    side=random.randrange(30,100)
    polly= random.randrange(3,10)
    angle=360/polly
    repeats=1
    while repeats < polly+1:
        forward(side)
        left(angle)
        repeats = repeats+1
    direction = random.randrange(0,360)
    setheading(direction)
    run = random.randrange(10,50)
    penup() 
    forward(run)
    pendown()
    bow = bow +1
    rain = bow % 6
    end_fill()
done()
