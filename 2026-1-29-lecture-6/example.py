# Read integers until the user enters 0
# prints the count of the numbers entered
# prints the maxiumum number entered

# we will need to loop
# - For for or while?
#   - while loop (sential)

# store all numbers in a list and run at the end
# i know that i can get the max of a list
# i know that i can get the len of a list

# keep a count and max variable and update them each loop
# i know that i can store and increment a count
# I know that i can check if a number is larger than another

user_input = input('> ').strip()
nums = []

while user_input != '0':
    # work
    if user_input.isnumeric():
        num = int(user_input)
        nums.append(num)

    user_input = input('> ').strip()

highestNumber = None
if (len(nums) > 0):
    highestNumber = max(nums)

print("max: ", highestNumber)
print("count: ", len(nums))