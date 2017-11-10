maand = eval(input('Welk maandnummer is het?:\n'))
def seizoen(maand):
    if maand == 12 or maand == 1 or maand == 2:
        x = 'Winter'
    elif maand == 3 or maand == 4 or maand == 5:
        x = 'Lente'
    elif maand == 6 or maand == 7 or maand == 8:
        x = 'Zomer'
    elif maand == 9 or maand == 10 or maand == 11:
        x = 'Herfst'
    return x

print('Het is {}'.format(seizoen(maand)))