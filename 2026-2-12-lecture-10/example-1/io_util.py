def print_factorial_equation(num):
    for i in range(1, num + 1):
        print(f"{i}", end = " ")
        
        if i != num:
            print("*", end=" ")

    print("=", end=" ")

def number_input(msg):
    print(msg)
    user_input = input("> ")
    if user_input.isnumeric():
        return int(user_input)
    else:
        print("Invalid number")
        exit()