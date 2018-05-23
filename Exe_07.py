Weekday = ['Monday','Tuesday','Wednesday','Thursday','Friday']
print(Weekday[0])

fruit = ['pineapple','pear']
fruit.insert(1,'grape')
print(fruit)

fruit[0:0] = ['Orange']
print(fruit)

fruit = ['pinapple','pear','grape']
fruit.remove('grape')
print(fruit)

fruit[0] = 'Grapefruit'
print(fruit)

del fruit[0:2]
print(fruit)

periodic_table = ['H','He','Li','Be','B','C','N','O','F','Ne']
print(periodic_table[0])
print(periodic_table[-2])
print(periodic_table[0:3])
print(periodic_table[-10:-7])
print(periodic_table[-10:])
print(periodic_table[:9])
