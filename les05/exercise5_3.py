infile = open('kaartnummers.txt','r')
regels = infile.readlines()
infile.close()
lengte = len(regels)
regelnummer = 0
hoogstenummer = 0
for regel in regels:
    gegevens = regel.split(',')
    nummer = int(gegevens[0])
    regelnummer += 1
    if nummer > hoogstenummer:
        hoogstenummer = nummer
        eindnummer = regelnummer

print ('Deze file telt {} regels\nHet grootste kaartnummer is: {} en dat staat op regel {}'.format(lengte,hoogstenummer,eindnummer))