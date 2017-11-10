gewicht = eval(input('wat is uw gewicht?: '))
lengte = eval(input('wat is uw lengte?: '))
BMI = int(gewicht)/(float(lengte**2))
print(BMI)
if BMI > 25:
    print('overgewicht')
elif BMI > 18.5 and BMI < 25:
    print('normaal')
else:
    print('ondergewicht')