tabel = [[4, 7, 2, 5], [5, 1, 9, 2], [8, 3, 6, 6]]
for rij in range(len(tabel)):
    for kolom in range(len(tabel[0])):      # voor een 2D lijst zijn de kolommen altijd even lang (voorwaarde)
        print(tabel[rij][kolom], end = ' ')
    print()