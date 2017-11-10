bedrag = eval(input('Wat is het bedrag?: '))
percentage = eval(input('Wat is het rentepercentage?: '))

def eindbedrag(bedrag, percentage):
    som = bedrag + (percentage*bedrag)/100
    return som

print(eindbedrag(bedrag, percentage))