def kwadraten_som(grondgetallen):
    uitkomst = 0
    for getal in grondgetallen:
        if getal > 0:
            uitkomst += getal*getal
    return uitkomst

print(kwadraten_som([6, -6, 9, -4]))