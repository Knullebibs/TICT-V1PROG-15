try:
    bedrag = 4356
    aantal = eval(input('Voer het aantal mensen in:'))
    if aantal < 0:
        print('Negatieve getallen zijn niet toegestaan!')
    else:
        print(bedrag/aantal)
except ZeroDivisionError:
    print('Delen door nul kan niet!')
except NameError:
    print('Gebruik cijfers voor het invoeren van het aantal!')
except:
    print('Onjuiste invoer!')