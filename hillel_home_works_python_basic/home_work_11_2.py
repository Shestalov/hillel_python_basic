import random
import string

# keys_dict_1 = ['a', 'b', 'c', 'u', 'n']
keys_dict_1 = [random.choice(string.ascii_letters).lower() for char in range(10)]

# keys_dict_2 = ['a', 'b', 'c', 'j', 'w']
keys_dict_2 = [random.choice(string.ascii_letters).lower() for _ in range(10)]


dict_1 = {}
dict_2 = {}

for char in keys_dict_1:
    dict_1[char] = random.randint(0, 10)

print("Dict_1: ", dict_1)

for char in keys_dict_2:
    dict_2[char] = random.randint(0, 10)

print("Dict_2: ", dict_2)


new_dict = dict_1.copy()

for k, v in dict_2.items():

    if k in new_dict and dict_2[k] > new_dict[k]:
        new_dict[k] = v
    elif k in new_dict and dict_2[k] < new_dict[k]:
        continue
    else:
        new_dict.update({k: v})


print("New_dict: ", new_dict)
