my_string = "Lorem Ipsum is simply dummy ipsum text of the printing ipsum and typesetting industry ipsum. " \
       "Lorem Ipsum has been the lorem ipsum."

# my_string = input("Text: ")

counter_dict = {}

for word in my_string.replace(".", " ").lower().split():

    counter_dict[word] = counter_dict.get(word, 0) + 1


for k, v in counter_dict.items():

    print(k, v)
