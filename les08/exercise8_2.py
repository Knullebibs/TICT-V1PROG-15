import random

def monopolyworp():
    dubbel = 0
    a = random.randrange(1, 7)
    b = random.randrange(1, 7)
    while True:
        if a == b and dubbel < 2:
            print('{} + {} = {} (dubbel)'.format(a, b, a+b))
            dubbel += 1
        elif a==b and dubbel == 2:
            print('{} + {} = (direct naar gevangenis)'.format(a, b))
            break
        else:
            print('{} + {} = {}'.format(a, b, a+b))
            break

monopolyworp()
