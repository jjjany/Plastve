# Plástev
from turtle import shape, forward, left, right, exitonclick, penup, pendown

shape('turtle')
right(60)
for i in range(6):
    forward(50)
    left(60)

right(120)

for i in range(6):
    penup()
    forward(50)
    pendown()
    right(60)    
    for i in range(4):
        forward(50)
        right(60)
    right(120)

penup()
forward(50)
right(60)
forward(50)
left(60)
forward(50)

for i in range(6):
    pendown()
    for i in range(4):
        right(60)
        forward(50)    
    right(180)
    penup()
    forward(50)
    pendown()
    for i in range(3):
        right(60)
        forward(50)
    right(180)
    penup()
    forward(50)
    
exitonclick()