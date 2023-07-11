# Поиск рандомного целочисленного числа

import random

x = random.randint(0,10)

print(x)

# Поиск рандомного элемента из заданного списка 

import random

x = [1, 4, 8, 'мама', 'папа']
print("Случайное число из списка", random.choice(x))

# Генератор случайного дробного числа
# x = random.random()
# print (x)

# Для дробных чисел

import random

y = random.uniform(1.5, 5.5)
print(round(y, 2))
