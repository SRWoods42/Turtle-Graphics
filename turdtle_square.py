from turtle import *

pencolor("white")
pensize(5)
bgcolor('black')
fillcolor('yellow')
begin_fill()

forward (150)
left (90)
forward (150)
left (90)
forward (150)
left (90)
forward (150)
left (90)


for i in range(2):
    forward (225)
    left (90)
   

for c in ["yellow", "red", "purple","orange"]:
    color(c)
    forward(200)
    left(90)
 

# Assign a list to a variable
clrs = ["violet", "orange", "blue", "white"]
for c in clrs:
    color(c)
    forward(250)
    left(90)























"""
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
"""
