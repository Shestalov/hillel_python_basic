pupils = int(input("How many pupils?: "))
apples = int(input("How many apples?: "))

basket = apples % pupils
apples_for_pupils = apples // pupils

print("The rest of the apples in the basket: ", basket)
print("Apples for each pupil: ", apples_for_pupils)

