import csv
with open('gamers.csv', 'r') as myCSVFile:
    reader = csv.reader(myCSVFile, delimiter=';')
    max = 0
    naam = ''
    for regel in reader:
        score = max + int(regel[2])
        speler = naam + str(regel[0])

print('De hoogste score is: {} behaald door {}'.format(score, speler))