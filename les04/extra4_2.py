temp = eval(input('Hoeveel graden is het vandaag?: '))
def f(x):
    if x < 0:
        print('Het vriest vandaag.')
    elif x >= 0 and x <= 15:
        print('Het is koud vandaag.')
    else:
        print('Het is lekker weer vandaag.')

f(temp)
f(12)
