def berekensomonevengetallen(som1):
    som1 = 0
    for getal in getallenrij:
        if getal %2 != 0:
            som1 = som1 + getal
    return som1
getallenrij = [23, 35, 31, 26, 73, 75, 84, 29, 42, 46]
print('De som van de oneven getallen bedraagt {}'.format(berekensomonevengetallen(getallenrij)))
def berekensomevengetallen(som):
    som = 0
    for getal in getallenrij:
        if getal %2 == 0:
            som = som + getal
    return som
getallenrij = [23, 35, 31, 26, 73, 75, 84, 29, 42, 46]
print('De som van de even getallen bedraagt {}'.format(berekensomevengetallen(getallenrij)))