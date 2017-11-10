def som(getallenlijst):
    optelling = 0
    for getal in getallenlijst:
        optelling += getal
    return optelling

getallenlijst = [6, 3, 8]
print(som(getallenlijst))