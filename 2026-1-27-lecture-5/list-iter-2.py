print("Input numbers:")
user_input = input("> ")

tokens = user_input.split() # Split input into list of strings

numbers = []
for token in tokens:
	if token.isnumeric():
		number = int(token)
		numbers.append(number)
	else:
		print(f"'{token}' is not a valid number. Ignoring.")

## find heighest multiple of 10
highest_multiple_of_10 = None
for number in numbers:
	if number % 10 == 0 and (highest_multiple_of_10 is None or number > highest_multiple_of_10):
		highest_multiple_of_10 = number

if highest_multiple_of_10 is not None:
	print(f"The highest multiple of 10 is: {highest_multiple_of_10}")
else:
	print("No multiples of 10 were entered.")