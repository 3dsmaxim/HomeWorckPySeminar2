# Задача 14
# Требуется вывести все целые степени двойки
# (т.е. числа вида 2 в степени k), не превосходящие числа N.
# 5
# 1 2 4

# 17
# 1 2 4 8 16


def NumEnter(n):
    while True:
        try:
            if int(n) >= 0:
                break
            if int(n) < 0:
                n = input('Введите целое число от 1-го и выше: ')
        except:
            n = input('Ввод не верный, повторите ввод: ')
    return int(n)


def PowTwo(k):
    if k == 0:
        print('1')
    elif k == 1:
        print('1, 2')
    else:
        print(end='1, 2')
        i = 2
        while pow(2, i) <= k:
            print(end=f', {pow(2, i)}')
            i += 1


number = NumEnter((input('Введите целое положительное число: ')))
PowTwo(number)
