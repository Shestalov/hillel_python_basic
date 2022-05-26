"""
Програма запитує введення, з клавіатури, цілі числа, поки не буде введено 0.

Як тільки буде введено 0 (нуль), програма повинна порахувати та вивести на екран:

-кількість введених чисел (завершальний 0 не рахується)
-їхню суму
-середнє арифметичне всіх введених чисел (за винятком завершального числа 0)
-визначити максимальне та мінімальне значення
-визначити кількість парних та непарних елементів у послідовності
"""

counter = 0
sum_attempts = 0
max_attempt = 0
min_attempt = 100
odd = 0
even = 0

while True:

    counter += 1

    ask = int(input('Try only integers: '))

    sum_attempts += ask

    # check max integer
    if ask > max_attempt:
        max_attempt = ask

    # if ask will be more 100
    if ask > min_attempt:
        min_attempt += ask

    # check min integer
    if ask < min_attempt and ask != 0:
        min_attempt = ask

    # check even
    if ask % 2 == 0 and ask != 0:
        even += 1

    # check odd
    if ask % 2 == 1:
        odd += 1

    if ask == 0:
        print("Attempts:", counter-1)
        print("Sum attempts:", sum_attempts)
        print("Arithmetic mean:", sum_attempts/(counter-1))
        print("Min int:", min_attempt)
        print("Max int:", max_attempt)
        print("Number of even int:", even)
        print("Number of odd int:", odd)
        break


