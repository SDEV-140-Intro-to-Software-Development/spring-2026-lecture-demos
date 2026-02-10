user_input = None

def print_name():
    print("Eric")
    print("Jordyn")
    print("Dustin")


def math():
    if user_input < 0:
        return None

    return 5 + 3

user_input = int(input("> "))
x = math()
print(x)