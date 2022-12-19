# Задача 12
# Петя и Катя – брат и сестра. 
# Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y(X, Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа

from cmath import sqrt
import random


def NamberHidden():
    num = []
    for i in range(2):
        num.append(random.randint(0, 1000))
    return num


def QuadraticEquation(chisla):
    num = (sqrt(pow(chisla[0] + chisla[1], 2) - 4 * chisla[0] * chisla[1]) \
            + chisla[0] + chisla[1])/ 2


    return num




numbers = NamberHidden()
# print(numbers)
print(f'Мясной мешок Петя(родители знали как назвать это) \
      \nзагадал мааааленькой сестре Кате 2 числа от 0 до 1000. \
       \nон дал 2 подсказки: \n1. Сумма этих чисел чисел равна {numbers[0] + numbers[1]} \
        \n2. Произведение этих чисел равна {numbers[0] * numbers[1]}')
numberFyrst = QuadraticEquation(numbers)

print(f'\nКатя полистала справочник по математике \
          \nи хотела дать единственный верный ответ \
          \nотражающий личностные качества её брата \
          \nно Катя воспитанная девачка и ответила, \
          \nчто числа которые загадал ее брат это: \
 {str(numberFyrst)[1: -4]} и  {numbers[0] + numbers[1] - int(str(numberFyrst)[1: -4])}')


 