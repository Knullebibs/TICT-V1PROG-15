cijferICOR = 6
cijferPROG = 7
cijferCSN = 6

gemiddelde = ((cijferICOR + cijferPROG + cijferCSN) /3)
beloning = gemiddelde*30
overzicht = 'Mijn cijfers (gemiddeld een ' + str(gemiddelde) + ') leveren een beloning van €' + str(beloning) + '0 op!'

print(gemiddelde)
print(beloning)
print(overzicht)