##创建10个文本##
def text_creation():
    path = '/Users/Public/Desktop/'
    for name in range(1, 11):
        with open(path + str(name) + '.txt', 'w') as text:
            text.write(str(name))
            text.close()
            print('Done')


text_creation()


##复利公式##
def invest(amount, rate, time):
    print("Principal amount:{}".format(amount))
    for t in range(1, time + 1):
        amount = amount * (1 + rate)
        print("year {}: ${}".format(t, amount))


invest(100, .05, 8)
invest(2000, .025, 5)


##打印1-100中的所有偶数##
def even_print():
    for i in range(1, 101):
        if i % 2 == 0:
            print(i)


even_print()

##猜大小##
a_list = [1, 2, 3]
print(sum(a_list))


import random
point1 = random.randrange(1,7)
point2 = random.randrange(1,7)
point3 = random.randrange(1,7)
print(point1,point2,point3)


import random
def roll_dice(numbers=3, points=None):
    print('<<<<<ROLL THE DICE!>>>>>')
    if points is None:
        points = []
    while numbers > 0:
        point = random.randrange(1,7)
        points.append(point)
        numbers =numbers - 1
    return points

def start_game():
    print('<<<<<GAME STARTS!>>>>>')
    choices = ['Big', 'Small']
    your_choice = input('Big or Small:')
    if your_choice in choices:
        points = roll_dice()
        total = sum(points)
        youWin = your_choice == roll_result(total)
        if youWin:
            print('The points are',points,'You Win!')
        else:
            print('The points are',points,'You lose!')
            else:
                print('Invalid Words')
        start_game()
Start_game()