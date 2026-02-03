# A calculator where a user can submit a list of numbers
# and we we get the sum and average of those numbers
# if user types stop, stop loop and output results

sum = 0
count = 0

print("Enter a number or type stop to finish.")
user_input = input("> ").lower().strip()

while user_input != "stop":
    if user_input.isnumeric():
        num = float(user_input)
        sum += num
        count += 1
    else:
        print(f"\"{user_input}\": is not a valid number.")

    print("Enter a number or type stop to finish.")
    user_input = input("> ").lower().strip()

if count == 0:
    print(f"Sum: {0}")
    print(f"Average: {0}")
else:
    print(f"Sum: {sum}")
    print(f"Average: {sum/count}")
