class_1 = int(input("How many pupils are in the first class?: "))
class_2 = int(input("How many pupils are the second class?: "))
class_3 = int(input("How many pupils are in the third class?: "))

total_pupils = class_1 + class_2 + class_3

desks = total_pupils // 2
left_pupil = total_pupils % 2

total_desk = left_pupil + desks

print(f"We need {total_desk} desks for three math classes.")
