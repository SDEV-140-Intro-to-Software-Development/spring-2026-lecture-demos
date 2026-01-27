user_input = input("Enter numbers separated by spaces: ")
tokens = user_input.split()
numbers = [int(token) for token in tokens if token.isnumeric()]
print("Valid numbers are:", numbers)