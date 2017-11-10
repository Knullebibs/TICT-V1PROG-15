def standaardtarief(afstandKM):
    if afstandKM <= 50:
        standaardtarief = 0.8 * afstandKM
    elif afstandKM > 50:
        standaardtarief = 15 + 0.6 * afstandKM
    elif afstandKM <= 0:
        standaardtarief = 0
    return standaardtarief

def ritprijs(leeftijd, weekendrit, afstandKM):
    if leeftijd > 65 or leeftijd < 12 and weekendrit == 'ja' or weekendrit == 'Ja':
        ritprijs = standaardtarief(afstandKM) * 0.65
    elif leeftijd > 65 or leeftijd < 12 and weekendrit == 'nee' or weekendrit == 'Nee':
        ritprijs = standaardtarief(afstandKM) * 0.7
    elif leeftijd < 65 and leeftijd > 12 and weekendrit == 'ja' or weekendrit == 'Ja':
        ritprijs = standaardtarief(afstandKM) * 0.6
    elif leeftijd < 65 and leeftijd > 12 and weekendrit == 'nee' or weekendrit == 'Nee':
        ritprijs = standaardtarief(afstandKM)
    return ritprijs

leeftijd = eval(input('Wat is uw leeftijd? '))
afstandKM = eval(input('Wat is de afstand in kilometers? '))
weekendrit = input('Reist u in het weekend? ')

print('De totale prijs die u moet betalen is {} euro'.format(ritprijs(leeftijd, weekendrit, afstandKM)))
