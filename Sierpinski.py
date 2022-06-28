#draw a sierpinsky triangle with a given size and number of iterations
from turtle import *
pencolor('yellow')
pensize(1)
bgcolor('black')


def drawsierp(s,m):
    repeat=1
    again=1
    if m==0:
          while repeat<4:
              forward(s)
              right(120)
              repeat=repeat+1
    else: 
          while again <4:
              drawsierp(s/2,m-1)
              forward(s)
              right(120)
              again=again+1



size=int(input("How big a triangle? Give me a number between 200 and 500   "))
iterations=int(input("and how many iterations? Give me a number between 1 and 10   "))

penup()
left (90)
forward (200)
left (90)
forward (200)
right (180)
pendown()



drawsierp(size, iterations)
    
done()
