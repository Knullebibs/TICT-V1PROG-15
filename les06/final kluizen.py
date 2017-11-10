def toon_aantal_kluizen_vrij():
    print(1)
    infile = open('kluizen.txt','r')
    kluizendata = infile.readlines()
    infile.close()
    aantalkluizen = len(kluizendata)
    aantalvrij = 12 - aantalkluizen
    print(aantalvrij)

def nieuwe_kluis():
    print(2)


def kluis_openen():
    print(3)
    infile = open('kluizen.txt','r')
    kluizendata = infile.readlines()
    infile.close()
    stringnummer = input('Wat is je nummer?: ')
    code = input('Wat is je code?: ')
    gegevenscorrect = False
    for kluis in kluizendata:
        gegevensvan1kluis = kluis.split(';')
        stringkluisnummer = gegevensvan1kluis[0]
        kluiscode = gegevensvan1kluis[1].strip()
        if stringnummer == stringkluisnummer and code == kluiscode:
            gegevenscorrect = True
    if gegevenscorrect:
        print('De kluis wordt geopend!')
    else:
        print('De kluis wordt niet geopend')

def kluis_teruggeven():
    # het inlezen van kluizen.txt in een list kluizendata met readlines()
    # elk element van de lijst is een regel uit kluizen.txt
    infile = open('kluizen.txt', 'r')
    kluizendata = infile.readlines()
    infile.close()
    # vraag aan de gebuiker het nummer van de kluis
    stringnummer = input('Wat is het nummer van je kluis: ')
    # vraag aan de gebuiker de code van de kluis
    code = input('Wat is de code van je kluis: ')
    # er wordt een nieuw lege lijst aangemaakt. In deze lijst worden alle gegevens van
    # het invoerbestand gestopt, behalve die van de kluis die teruggegevens wordt.
    nieuwekluizendata = []
    # alle regels van het tekstbestand worden doorlopen
    for kluis in kluizendata:
        # doorlopen van kluizendata en elke regel van kluizendata splitsen op ';'
        datavan1kluis = kluis.split(';')
        # elke regel bestaat uit twee elementen waarvan het 1e element het nummer is van het type string;
        stringkluisnummer = datavan1kluis[0]
        # het tweede element is de kluiscode met \n erachter. Die gaat eraf m.b.v. strip.
        kluiscode = datavan1kluis[1].strip()
        # gegevenscorrect is true als nummer en code overeenkomen
        gegevenscorrect = (stringkluisnummer == stringnummer) and (kluiscode == code)
        # als de gegevens niet overeen komen, worden de gegevens aan de lijst nieuwekluizendata toegevoegd
        if not gegevenscorrect:
            # elk element van deze lijst bestaat uit een (string)nummer en een code gescheiden door puntkomma.
            nieuwekluizendata.append(stringkluisnummer + ';' + kluiscode)
    # de list nieuwekluizendat bevat nu alle regels van het invoerbestand, behalve van de kluis
    # die teruggegeven is.
    # Het bestand kluizen.txt wordt nu geopend, maar dan voor schrijven.
    # De bestaande inhoud is hiermee gewist
    outfile = open('kluizen.txt', 'w')
    for i in range(0, len(nieuwekluizendata)):
        # alle elementen worden weggeschreven. Door \n komt ieder volgend element op een volgende regel terecht.
        outfile.write(nieuwekluizendata[i] + '\n')
    # het bestand wordt gesloten.
    outfile.close()

print('1: hoeveel vrij')
print('2: nieuwekluis')
print('3: kluisopenen')
keuze = eval(input('maakkeuze: '))
if keuze == 1:
    toon_aantal_kluizen_vrij()
elif keuze == 2:
    nieuwe_kluis()
else:
    kluis_openen()