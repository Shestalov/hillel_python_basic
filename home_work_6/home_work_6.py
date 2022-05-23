"""
Програма запитує введення, з клавіатури, цілі числа, поки не буде введено 0.

Як тільки буде введено 0 (нуль), програма повинна порахувати та вивести на екран:

-кількість введених чисел (завершальний 0 не рахується)
-їхню суму
-середнє арифметичне всіх введених чисел (за винятком завершального числа 0)
-визначити максимальне та мінімальне значення
-визначити кількість парних та непарних елементів у послідовності
"""

l =[]


while True:

    ask = int(input('Try only integers: '))

    if ask == 0:

        even = len([x for x in l if x % 2 == 0])
        odd = len([x for x in l if x % 2 == 1])

        print("Attempts:",len(l))
        print("Sum attempts:",sum(l))
        print("Arithmetic mean:",sum(l)/len(l))
        print("Min int:",min(l))
        print("Max int:",max(l))
        print("Number of even int:",even)
        print("Number of odd int:",odd)
        break
    
    else:
        l.append(ask)


