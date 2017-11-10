def code(invoerstring):
    antwoord = ''
    for letter in invoerstring:
        cr = ord(letter) + 3
        antwoord += chr(cr)
    return antwoord

print(code("RutteAlkmaarDen Helder"))