set_1 = {1, 2, 3, 4}
set_2 = {1, 2, 3}

# one line
print(set_2 - set_1 == set())

# only if else
if set_1 >= set_2:
    print("True")
else:
    print("False")


# function
def superset(first_set, second_set):
    if first_set >= second_set:
        return True
    else:
        return False


my_func = superset(set_1, set_2)
print(my_func)

# checking (set_1 is a superset for set_2)
print(set_1.issuperset(set_2))
