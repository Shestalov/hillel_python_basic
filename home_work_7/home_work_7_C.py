height = int(input('Number: '))

for num in range(1, height+1):

    for i in range(num, height+1):

        print(' ', end=' ')

    for i in range(1, num+1):

        print('*', end=' ')

    for i in range(1, num):

        print('*', end=' ')

    print()

for num in range(2, height+1):

    for i in range(num):

        print(' ', end=' ')

    for i in range(num, height+1):

        if num == i:
            print('*', end=' ')
        else:
            print(' ', end=' ')

    for i in range(num, height+1):

        if i == height-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')

    print()