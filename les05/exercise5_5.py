zin = input('Schrijf een zin:\n')
woorden = zin.split()
letters = 0
aantalwoorden = len(woorden)
for woord in woorden:
    letters += len(woord)
antwoord = letters/aantalwoorden
print(antwoord)