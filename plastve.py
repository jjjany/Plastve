from turtle import distance, forward, penup, pendown, exitonclick, left, right

# n vrstev pláství

while True:
    lr = int(input('Zadej počet vrstev pláství. (Celé nezáporné číslo.)'))
    ds = 40  # ds je číslo udávající délku strany v jednotkách želvy (pixelech?)

    if lr < 0:
        print('Počet vrstev musí být celé nezáporné číslo.')
    else:
        break

def pla(ds):  # tato funkce nakreslí právě 1 plástev (šestiúhelník) o délce strany ds
    for i in range(6):
        forward(ds)
        left(60)


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