num_list = [8, 2, 1, 3, 4, 7, 6]

for index, value in enumerate(num_list):
    if index == value:
        print("*", end="")

    print(value, end=" ")


# ---
# index = 0
# value = 8
# index == value ? no
# output: 8 
# ---
# index = 1
# value = 2
# output: 2