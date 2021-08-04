from turtle import distance, forward, penup, pendown, exitonclick, left, right

# n vrstev pláství

while True:
    
    ds = 15  # ds je číslo udávající délku strany v jednotkách želvy (pixelech?)
    try:
        lr = int(input('Zadej počet vrstev pláství. (Celé nezáporné číslo.)'))
        if lr < 0:
            print('Počet vrstev musí být celé nezáporné číslo.')
        elif lr == 0:
            print('Není, co kreslit.')
        else:
            break
    except ValueError:
        print('To nebylo celé nezáporné číslo!')

def pla(ds):  # tato funkce nakreslí právě 1 vrstvu pláství, tj. 1 plástev (šestiúhelník) o délce strany ds
    for i in range(6):
        forward(ds)
        left(60)

def pla_lrn(lr):  # tato funkce nakreslí n-tou vrstvu pláství pro n>=1
    for i in range(6):
        for i in range(lr-1):
            pla(ds)
            forward(ds)
            left(60)
            forward(ds)
            right(60)
        forward(ds)
        left(60)


for i in range(lr):
    pla_lrn(lr-i)
    left(120)
    forward(ds)
    right(60)
    forward(ds)
    right(60)

exitonclick()