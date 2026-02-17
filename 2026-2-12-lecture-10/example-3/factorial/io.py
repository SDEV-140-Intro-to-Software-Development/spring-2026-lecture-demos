def print_factorial_equation(num):
    for i in range(1, num + 1):
        print(f"{i}", end = " ")
        
        if i != num:
            print("*", end=" ")

    print("=", end=" ")

def float_input(msg):
    print(msg)
    user_input = input("> ")
    return float(user_input)

def int_input(msg):
    print(msg)
    user_input = input("> ")
    return int(user_input)

def positive_int_input(msg):
    value = int_input(msg)
    if value < 0:
        raise ValueError("Number most be positive")

    return value