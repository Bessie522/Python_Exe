
NASDAQ_code = {
    'BIDU':'Baidu',
    'SINA':'Sina',
    'YOKU':'YouKu'
}

a = {'key':123,'key':123}
print(a)

NASDAQ_code = {'BIDU':'Baidu','SINA':'Sina'}
NASDAQ_code['YOKU'] = 'Youku'
print(NASDAQ_code)

NASDAQ_code.update({'FB':'Facebook','TSLA':'Tesla'})
print(NASDAQ_code)

del NASDAQ_code['FB']
print(NASDAQ_code)

letters = ('a','b','c','d','e','f','g')
letters[0]
print(letters)

a_set = {1,2,3,4}
a_set.add(5)
print(a_set)
a_set.discard(5)
print(a_set)