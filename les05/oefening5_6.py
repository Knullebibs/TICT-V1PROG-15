infile = open('kaarnummers.txt', 'r')
regels = infile.readlines()
infile.close()
outfile = open('kaartnummersuit.txt', 'w')
for regel in regels:
    kaartinfo = regel.split(',')
    outfile.write('[] heeft kaarnummer: []/n'.format(kaartinfo[1].strip(),kaartinfo[0]))
outfile.close