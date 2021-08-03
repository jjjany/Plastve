from turtle import distance, forward, penup, pendown, exitonclick, left, right
#Plástve

def pla(ds):
    #ds je číslo udávající délku strany v jednotkách želvy (pixelech?)
    for i in range(6):
        forward(ds)
        left(60)

#n vrstev pláství
while True:
    lr = int(input('Zadej počet vrstev pláství. (Celé nezáporné číslo.)'))
    ds = 40

    if lr < 0:
        print('Počet vrstev musí být celé nezáporné číslo.')
    else:
        break

#for i in range(lr):

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