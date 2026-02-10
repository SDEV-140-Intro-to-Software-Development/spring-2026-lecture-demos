def print_menu():
    print("Today's Menu:")
    print("   1) Gumbo")
    print("   2) Jambalaya")
    print("   3) Quit\n")
    print("What would you like?")


print_menu()
user_choice = int(input("> "))
cart = []

while user_choice != 3:
    match user_choice:
        case 1:
            cart.append("Gumbo")
        case 2:
            cart.append("Jambalaya")
        case _:
            print("Unknown option")

    print_menu()
    print("Cart: ", cart)
    user_choice = int(input("> "))