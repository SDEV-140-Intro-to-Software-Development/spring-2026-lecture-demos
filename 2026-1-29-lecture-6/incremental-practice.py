def factioral(number):
    output = 1
    for x in range(2, number + 1):
        output *= x
    return output

print("Input a number you would like the factorial of: ")
user_input = input("> ")

if user_input.isnumeric():
    num = int(user_input)
    print(factioral(num))
else:
    print("WARN: This is not a number")