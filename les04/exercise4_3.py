lengte = eval(input('Wat is uw lengte (in cm)?: '))
def lang_genoeg(lengte):
    return lengte
if lang_genoeg(lengte) >= 120:
    print('Je bent lang genoeg voor de attractie!')
else:
    print('Sorry, je bent te kort!')
