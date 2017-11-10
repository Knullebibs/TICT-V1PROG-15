def namen():
    dictionary = {}
    naam = input('Volgende naam: ')
    while naam != '':
        naam = input('Volgende naam: ')
        if naam in dictionary:
            dictionary[naam] += 1
        else:
            dictionary[naam] = 1
    for naam in dictionary:
        if dictionary[naam] == 1:
            print('Er is {} student met de naam {}'.format(dictionary[naam], naam))
        else:
            print('Er zijn {} studenten met de naam {}'.format(dictionary[naam], naam))
namen()
