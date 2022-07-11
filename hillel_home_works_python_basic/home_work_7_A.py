height = int(input("Number: "))

for num in range(1, height+1):

    for i in range(1, height*2):

        if num == height or num + i == height+1 or i-num == height-1:
            print(' * ', end='')
        else:
            print(end='   ')

    print()

