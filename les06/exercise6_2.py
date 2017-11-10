# lijst = ["boter", "kaas", "bier", "pizza", "thee", "drop", "koek", "cola", "boterham", "stamppot"]
lijst = eval(input("Geef lijst met minimaal 10 strings:\n"))
nieuwelijst = []
for woord in lijst:
    if len(woord) == 4:
        nieuwelijst.append(woord)

print('De nieuw-gemaakte lijst met alle vier-letter strings is: {}'.format(nieuwelijst))