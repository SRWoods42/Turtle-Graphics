#draw a sierpinsky-type polygon line fractal for a given polygon, with a given size and number of iterations
from turtle import *
pencolor('yellow')
pensize(1)
bgcolor('black')


def polysierp(v,s,m):
    repeat=1
    again=1
    if m==0:
          while repeat<v+1:
              forward(s)
              right(360/v)
              repeat=repeat+1
    else: 
          while again <v+1:
              polysierp(v, s/2,m-1)
              forward(s)
              right(360/v)
              again=again+1



size=int(input("How big a polygon? Give me a number between 200 and 500   "))
iterations=int(input("and how many iterations? Give me a number between 1 and 10   "))
vertices=int(input(" and the polygon, how many sides? Give me a number greater than 2   "))

penup()
left (90)
forward (200)
left (90)
forward (200)
right (180)
pendown()



polysierp( vertices, size, iterations)
    
done()
