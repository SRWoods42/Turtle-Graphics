from turtle import *
pencolor('red')
pensize(5)
bgcolor('black')
fillcolor('yellow')

angle = 0
rainbow =["red", "orange", "yellow", "green", "blue", "purple"]
bow = 0
rain=bow%6
side = 200

while side > 0:
    begin_fill()
    fillcolor(rainbow[rain])
    pencolor(rainbow[rain])
    forward(side)
    left(90)
    forward(side)
    left(90)
    forward(side)
    left(90)
    forward(side)
    left(90)
    angle= angle+10
    setheading(angle)
    side=side-1
    bow = bow +1
    rain = bow % 6
    end_fill()
done()
