# Алгоритм Евклида делением 
a = 35
b = 14
n = 0
while a != 0 and b != 0:
    n += 1
    print("Сейчас итерация: ", n)
    if a > b:
        a = a % b
        print(a)
    else:
        b = b % a
        print(b)
print("Итог", a + b)

# Алгоритм Евклида Вычитанием
a = 35
b = 14
while a != b:
    print("Значение а: ", a)
    print("Значение b: ", b)
    if a > b:
        a = a - b
    else:
        b = b - a
print(b)

a = int(input("Введи делимое:"))
b = int(input("Введи делитель:"))

try:
    x = a/b
    print("Результат: ", x)
except ZeroDivisionError:
    print("У вас деление на 0")
finally:
    print("Отработал блок файнали")
    a = int(input("Введи делимое:"))
    b = int(input("Введи делитель:"))
    x = a/b
    print("Результат: ", x)
    

