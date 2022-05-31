import random

numbers = [random.randint(0, 9) for _ in range(10)]

print(numbers)

counter = 0

for i in range(1, len(numbers)-1):

    if numbers[i] > numbers[i-1] and numbers[i] > numbers[i+1]:
        counter += 1

print('Result: ', counter)


