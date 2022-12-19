# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.



import random


def NumEnter(n):
    while True:
        try:
            if int(n) > 0:
                break
            if int(n) <= 0:
                n = int(input('Введите целое число от 1-го и выше: '))
        except:
            n = int(input('Ввод не верный, повторите ввод: '))
    return int(n)


def ArrayCoin(k):
    array = []
    i = 0
    for i in range(0, k):
        array.append(random.randint(0, 1))
    return array


def HowMachFlip(m):
    sum = 0
    for i in range(0, len(m)):
        if m[i] == 1:
            sum += 1
    if sum >= (len(m) - sum):
        print(
            f'Минемольное колличество монет которые надо перевенуть {len(m) - sum} шт.')
    else:
        print(
            f'Минемольное колличество монет которые надо перевенуть {sum} шт.')


num = NumEnter(input('Ввведите количество монет: '))
coin = ArrayCoin(num)
print(coin)
HowMachFlip(coin)
