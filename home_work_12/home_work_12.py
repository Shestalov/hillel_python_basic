set_1 = {1, 2, 3, 4}
set_2 = {2, 3, 4, 5}

i = set_1 & set_2

if i == set_1 == set_2:
    print("set 1 is a superset for set 2 and vice versa.")
elif i == set_1:
    print("set 2 is a superset for set 1")
elif i == set_2:
    print("set 1 is a superset for set 2")
else:
    print("False")

