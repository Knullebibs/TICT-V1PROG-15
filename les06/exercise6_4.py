studentencijfers = [[95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0]]

def gemiddelde_per_student(studentencijfers):
    antw = []
    totaal = 0
    for student in studentencijfers:
        for cijfer in student:
            totaal += cijfer
        antw.append(totaal / len(student))
        totaal = 0
    return antw

def gemiddelde_van_alle_studenten(studentencijfers):
    antw = sum(gemiddelde_per_student(studentencijfers)) / len(studentencijfers)
    return antw

print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))