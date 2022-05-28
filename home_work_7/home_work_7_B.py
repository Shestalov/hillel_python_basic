height = int(input("Number: "))

for num in range(1, height+1):

    for i in range(num, height+1):

        print(' ', end=' ')

    for i in range(1, num+1):

        print('*', end=' ')

    for i in range(1, num):

        print('*', end=' ')

    print()