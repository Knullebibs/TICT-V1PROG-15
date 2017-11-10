def convert(celsius):
    fahrenheit = celsius*1.8 + 32
    print('{:5} {:5}'.format(int(fahrenheit), celsius))
def table():
    print('   {:5} {}'.format('F', 'C'))
    for i in range(-30,41,10):
        convert(i)

table()