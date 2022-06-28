from turtle import *
pencolor('red')
pensize(5)
bgcolor('blue')
fillcolor('yellow')
begin_fill()
angle = 0
while angle <=360:
    forward(200)
    left(90)
    forward(200)
    left(90)
    forward(200)
    left(90)
    forward(200)
    left(90)
    angle= angle+10
    setheading(angle)
end_fill()
done()
