import csv

with open('9_4gegevens.csv', 'r') as myCSVFile:
    inhoud = csv.DictReader(myCSVFile, delimiter=';')
    prijs = {'Prijs' : '0'}
    voorraad = {'Voorraad' : '9999999999'}
    totaalvoorraad = 0
    for rij in inhoud:
        if eval(rij['Prijs']) > eval(prijs['Prijs']):
            prijs = rij
        elif eval(rij['Voorraad']) < eval(voorraad['Voorraad']):
            voorraad = rij
        totaalvoorraad += eval(rij['Voorraad'])

    print('Het duurste artikel is {} en die kost {} Euro'.format(prijs['Naam'],prijs['Prijs']))
    print('Er zijn slechts {} exemplaren in voorraad van het product met nummer {}'.format(voorraad['Voorraad'],voorraad['Artikelnummer']))
    print('In totaal hebben wij {} producten in ons magazijn liggen'.format(totaalvoorraad))