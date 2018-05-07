def fahrenheit_converter(c):
    fahrenheit = c * 9/5 + 32
    return str(fahrenheit) + '℉'

lyric_length = len('I Cry Out For Magic!')
print(lyric_length)

c2f = fahrenheit_converter(35)
print(c2f)

def fahrenheit_converter(c):
    fahrenheit = c * 9/5 + 32
    print(str(fahrenheit)+'℉')
c2f = fahrenheit_converter(35)
print(c2f)