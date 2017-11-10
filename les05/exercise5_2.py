infile = open('kaartnummers.txt', 'r')
regels = infile.readlines()
infile.close()
for regel in regels:
    gegevens = regel.split(', ')
    print(' {} heeft kaartnummer: {} '.format(gegevens[1].strip(), gegevens[0]))