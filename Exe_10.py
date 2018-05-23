class CocaCola():
    it_taste = 'So good!'
coke_for_bum = CocaCola()
coke_for_president = CocaCola()
print(coke_for_bum.it_taste)
print(coke_for_president.it_taste)

class CocaCola:
    formula = ['caffeine','sugar','water','soda']
coke_for_me = CocaCola()
coke_for_you = CocaCola()
print(CocaCola.formula)
print(coke_for_me.formula)
print(coke_for_you.formula)

for element in coke_for_me.formula:
    print(element)

class CocaCola:
    formula = ['caffeine','sugar','water','soda']
coke_for_China = CocaCola()
coke_for_China.local_logo = '可口可乐'  #创建实例属性
print(coke_for_China.local_logo)  #打印实例属性引用结果
print(coke_for_China.formula)

class CocaCola:
    formula = ['caffeine','sugar','water','soda']
    def drink(selfself):
        print('Energy!')
coke = CocaCola()
coke.drink()

class CocaCola:
    formula = ['caffeine','sugar','water','soda']
    def drink(coke):  #HERE
        print('Energy!')
coke = CocaCola()
coke.drink()

class CocaCola:
    formula = ['caffeine','sugar','water','soda']
    def drink(self,how_much):
        if how_much == 'a sip':
            print('Cool~')
        elif how_much == 'Whole bottle':
            print('Headache!')
ice_coke = CocaCola()
ice_coke.drink('a sip')
ice_coke.drink('Whole bottle')

class CocaCola:
    formula = ['caffeine','sugar','water','soda']
    def __init__(self):
        self.local_logo = '可口可乐'

    def drink(self):  #HERE
        print('Energy!')

coke = CocaCola()
print(coke.local_logo)


class CocaCola:
    formula = ['caffeine','sugar','water','soda']
    def __init__(self):
        for element in self.formula:
            print('Coke has {}!'.format(element))

    def drink(self):
        print('Energy!')
coke = CocaCola()


class CocaCola:
    formula = ['caffeine','sugar','water','soda']
    def __init__(self,logo_name):
        self.local_logo = logo_name
    def drink(self):
        print('Energy!')
coke = CocaCola('可口可乐')
coke.local_logo


class CocaCola:
    calories = 140
    sodium = 45
    total_carb = 39
    caffeine = 34
    ingredients = [
        'High fructose Corn Syrup',
        'Carbonated Water',
        'Phosphoric Acid',
        'Natural Flavors',
        'Caramel Color',
        'Caffeine']
    def _init_(self,logo_name):
        self.local_logo = logo_name
    def drink(self):
        print('You got () cal energy!'.format(self.calories))





