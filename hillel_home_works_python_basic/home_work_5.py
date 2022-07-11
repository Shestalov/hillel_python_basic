"""
За цілим числом N (не дробовим) роздрукуйте всі 
квадрати натуральних чисел, що не перевищують N, 
у порядку зростання.
"""

n = int(input('Input integer: '))

for num in range(1,n+1):

    res = num * num 
    
    if res > n:
        break
    else:
        print(res)
