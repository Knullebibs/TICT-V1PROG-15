som = 0
aantal = 0
getal = eval(input('Voer een cijfer in: '))
while getal != 0:
    som += getal
    getal = eval(input('Voer een cijfer in: '))
    aantal += 1
print('Er zijn {} getallen ingevoerd, de som is: {}'.format(aantal, som))