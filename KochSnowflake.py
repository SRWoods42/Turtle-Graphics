#draw a Kochsnowflake-type polygon line fractal for a given polygon, with a given size and number of iterations
from turtle import *
pencolor('pink')
pensize(1)
bgcolor('black')


def KochPoly(v,s,m):
    repeat=1
    
    if m==0:
        forward(s)

    else:
        KochPoly( v, s/v, m-1)
        left (180-360/v)
        while repeat<v-1:
            KochPoly(v, s/v, m-1)
            right (360/v)
            repeat=repeat+1
        KochPoly(v, s/v, m-1)
        left(180-360/v)
        KochPoly(v,s/v,m-1)

    



size=int(input("How big a polygon? Give me a number between 200 and 500   "))
iterations=int(input("and how many iterations? Give me a number between 1 and 10   "))
vertices=int(input(" and the polygon, how many sides? Three sides gives the classic Koch snowflake. Give me a number greater than 2   "))

penup()
left (90)
forward (200)
left (90)
forward (200)
right (180)
pendown()
v=vertices
again=1
while again<v+1:
    KochPoly( vertices, size, iterations)
    right (360/v)
    again=again+1
    
done()
