import random

# to enter the number of pupils and height for each pupil manually.
# pupils_in_the_line = int(input("How many pupils?: "))
# pupils_height = [int(input(f"Height of pupil {num+1}: ")) for num in range(pupils_in_the_line)]

# min height for pupil is 120 cm, max 200cm, 10 pupils in the line.
pupils_height = [random.randint(120, 200) for _ in range(10)]
pupils_height.sort(reverse=True)

print(f"The line of the pupils: \n{pupils_height}")

petro = int(input("What is the Petro's height (Min 120cm, Max 200cm): "))

for num in range(len(pupils_height)):

    # from 0 to the last num (exclusively)
    if pupils_height[num] < petro:
        pupils_height.insert(num, "Petro is here")  # for visualisation
        print(f"Petro is {num + 1} in the line.")
        break

    # for last num
    elif num == len(pupils_height) - 1:
        pupils_height.append("Petro is the last")  # for visualisation
        print(f"Petro is {len(pupils_height)} in the line.")

# show where is Petro in the line
print(f"The line of the pupils with Petro: \n{pupils_height}")
