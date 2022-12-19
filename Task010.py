import random


def numEnter(n):
    while True:
        try:
            if n > 1:
                break
            if n <= 0:
                n = int(input('Введите целое число от 1-го и выше: '))
        except:
            n = int(input('Ввод не верный, повторите ввод: '))
    return n


def arrayCoin(k):
    array = []
    i = 0
    for i in range(0, k):
        array.append(random.randint(0, 1))
    return array


def howMachFlip(m):
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


num = numEnter(int(input('Ввведите количество монет: ')))
coin = arrayCoin(num)
print(coin)
howMachFlip(coin)
