leeftijd = eval(input('Geef je leeftijd: '))
paspoort = input('Heb je een Nederlands paspoort?: ')
if (paspoort == 'ja' or paspoort == 'Ja') and leeftijd > 17:
    print('Gefeliciteerd! Je mag stemmen')
else:
    print('Helaas, je mag (nog) niet stemmen')