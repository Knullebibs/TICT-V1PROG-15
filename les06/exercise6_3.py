invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
nummers = invoer.split('-')
nummers.sort()
print('Gesorteerde list van ints: {}'.format(nummers))
print('Grootste getal: {} en Kleinste getal: {}'.format(max(nummers),min(nummers)))

aantal = 0
for getal in nummers:
    aantal += int(getal)
print('Aantal getallen: {} en Som van de getallen: {}'.format(len(nummers),aantal))

gemiddelde = aantal / len(nummers)
print('Gemiddelde: {}'.format(gemiddelde))