# This program asks the user to enter daily temperatures for one week.
# It should calculate and display the average temperature for the week.
# The program should ignore any temperatures below 0, since those readings are considered invalid.

total = 0
count = 0

for day in range(7):
    temp = int(input("Enter temperature for day " + str(day + 1) + ": "))

    if temp >= 0:
        total = total + temp

    count = count + 1

average = total / count

print("Average temperature:", average)
