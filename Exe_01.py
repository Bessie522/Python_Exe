def g_converter(kg):
    g = 0.001 * kg
    return str(g) + 'kg'


g2kg = g_converter(1)
print(g2kg)

import math


def triangle_third_side_length(bottom, high):
    side = math.sqrt(bottom * bottom + high * high)
    return str(side)


tts = triangle_third_side_length(3, 4)
print(tts)


def g2kg(g):
    return str(g / 1000) + 'kg'


print(g2kg(2000))  # 调用函数并打印结果


def pythagoren_theorem(a, b):
    return 'The right triangle third side\'s length is {}'.format((a ** 2 + b ** 2) ** (1 / 2))


# 等价a的平方与b的平方和的1/2次方（即开根）
print(pythagoren_theorem(3, 4))  # 调用函数打印结果


def fahrenheit_coverter(c):
    fahrenheit = c * 9 / 5 + 32
    return str(fahrenheit) + ' F'


print(fahrenheit_coverter(35))
print(fahrenheit_coverter(15))
print(fahrenheit_coverter(0))
print(fahrenheit_coverter(-3))


def trapezoid_area(base_up, base_down, height):
    return 1 / 2 * (base_up + base_down) * height


print(trapezoid_area(1, 2, 3))

base_up = 1
base_down = 2
height = 3

print(trapezoid_area(height, base_down, base_up))


def flashlight(battery1, battery2):
    return 'Light!'


nanfu1 = 600
nanfu2 = 600

print(flashlight(nanfu1, nanfu2))

print('  * ', ' ***  ', '*****   ', '  !   ', sep='\n')

file = open('/Users/Admin/Desktop/text.txt', 'w')
file.write('Hello World')


def text_create(name, msg):
    desktop_path = '/Users/Admin/Desktop/'
    full_path = desktop_path + name + '.txt'
    file = open(full_path, 'w')
    file.write(msg)
    file.close()
    print('Done')


text_create('hello', 'hello world')  # 调用函数


def text_filter(word, censored_word='lame', changed_word='Awesome'):
    return word.replace(censored_word, changed_word)


text_filter('Python is lame')  # 调用函数


def censored_text_create(name, msg):
    clean_msg = text_filter(msg)
    text_create(name, clean_msg)


censored_text_create('Try', 'lame!lame!lame!')  # 调用函数


def account_login():
    password = input('Password:')
    if password == '12345':
        print('Login success!')
    else:
        print('Wrong password or in valid input!')

        account_login()


account_login()


def account_login():
    password = input('Password:')
    password_correct = password == '12345'  # HERE!
    if password_correct:
        print('Login success!')
    else:
        print('Wrong password or invalid input!')
        account_login()


account_login()

password_list = ['*#*#', '12345']


def account_login():
    password = input('Password:')
    password_correct = password == password_list[-1]
    password_reset = password = password_list[0]
    if password_correct:
        print('Login success!')
    elif password_reset:
        new_password = input('Enter a new password:')
        password_list.append(new_password)
        print('Your password has changed successfully!')
        account_login()


account_login()


