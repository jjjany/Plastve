from turtle import distance, forward, penup, pendown, exitonclick, left, right
# plástve

def pla(ds):
    #ds je číslo udávající délku strany v jednotkách želvy (pixel?)
    for i in range(6):
        forward(ds)
        left(60)

#2 kruhy pláství (3 vrstvy)
ds=40
pla(ds)

forward(ds)
left(60)
forward(ds)
right(60)

for i in range(5):
    pla(ds)

    forward(ds)
    right(60)

left(120)
forward(ds)
right(60)

for i in range(6):
    for i in range(2):
        pla(ds)
        forward(ds)
        right(60)

    forward(ds)
    left(60)

forward(ds)
left(60)
forward(ds)
right(60)

exitonclick()