def ticker():
    infile = open('ticker.txt','r')
    regels = infile.readlines()
    infile.close()
    tickerdic = {}
    for regel in regels:
        regel = regel.strip()
        regel = regel.split(':')
        tickerdic[regel[0]] = regel[1]
    return tickerdic

print(ticker())
dictionary = ticker()

company = input('Enter Company name: ')
print('Ticker symbol: {}\n'.format(dictionary[company]))
Ticker = input('Enter Ticker symbol: ')
for key, value in dictionary.items():
    if value ==  Ticker:
        print('Company name: {}'.format(key))