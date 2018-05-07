word = 'friends'
find_the_evil_in_your_friends = word[0] + word[2:4] + word[-3:-1]
print(find_the_evil_in_your_friends)

phone_number = '1286-666-0006'
hiding_number = phone_number.replace(phone_number[:9], '*' * 9)
print(hiding_number)

search = '168'
num_a = '1386-168-0006'
num_b = '1681-222-0006'

print(search + ' is at ' + str(num_a.find(search)) + ' to ' + str(
    num_a.find(search) + len(search) + len(search)) + ' of num_a ')
print(search + ' is at ' + str(num_b.find(search)) + ' to ' + str(
    num_b.find(search) + len(search) + len(search)) + ' of num_b ')

print('{} a word she can get what she {} for.'.format('With', 'came'))
print('{preposition} a word she can get what she {verb} for.'.format(preposition='With', verb='came'))
print('{0} a word she can get what she {1} for.'.format('With', 'came'))

city = input("write down the name of city:")
url = "http://apistore.baidu.com/microservice/weather?citypinyin={}".format(city)

def fahrenheit_converter(c):
    fahrenheit = c * 9/5 + 32
    return str(fahrenheit) + 'F'

lyric_length = len('I Cry Out For Magic!')
print(lyric_length)

c2f = fahrenheit_converter(35)
print(c2f)




