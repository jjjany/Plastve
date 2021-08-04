from turtle import distance, forward, penup, pendown, exitonclick, left, right

# n vrstev pláství

while True:
    try:
        ds = float(input('Zadej délku strany (počet pixelů) plástve / šestiúhelníku. (Reálné nezáporné číslo.)'))  # ds je číslo udávající délku strany v jednotkách želvy (pixelech?)
        lr = int(input('Zadej počet vrstev pláství. (Celé nezáporné číslo.)'))
        if lr < 0 or ds < 0:
            print('Jedna ze zadaných hodnot je záporná. Zadej obě hodnoty znova!')
        elif lr == 0 or ds == 0:
            print('Po zadání nulové hodnoty, není, co kreslit.')
        else:
            break
    except ValueError:
        print('Vstupní hodnota nebyla zadána v požadovaném tvaru. Zkus to znovu!')

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

while True:
    odkud_kreslit = str(input('Mám jednotlivé vrstvy plástve začít kreslit od středu? (a/n)'))

    if odkud_kreslit == 'a' or odkud_kreslit == 'A':
        for i in range(lr):  # jednotlivé vrstvy kreslí od středu k povrchu
            pla_lrn(i+1)
            right(120)
            penup()
            forward(ds)
            left(60)
            forward(ds)
            pendown()
            left(60)
        break

    elif odkud_kreslit == 'n' or odkud_kreslit == 'N':
        for i in range(lr):  # jednotlivé vrstvy kreslím od povrchu ke středu
            pla_lrn(lr-i)
            left(120)
            forward(ds)
            right(60)
            forward(ds)
            right(60)
        break
    else:
        print('Nerozumím. Odpověz buď "a" jako ano, nebo "n" jako ne.')

exitonclick()