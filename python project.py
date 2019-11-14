import turtle
import random

fred = turtle.Turtle()
fred.speed(20)


colours = ["green", "yellow"]

length = 500
angle= 91
circle_size = 10

for side in range(length):
  #print(side)
  colour = random.choice(colours)
  fred.pencolor(colour)
  fred.penup()
  fred.forward(side)
  fred.pendown()
  fred.left(angle)
  fred.begin_fill()
  fred.circle(circle_size)
  fred.end_fill()
