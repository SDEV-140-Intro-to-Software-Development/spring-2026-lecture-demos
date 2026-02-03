age = int(input("Age? "))

if age < 0:
    print("Invalid age")
elif age <= 12:
    print("Child price")
elif age >= 65:
    print("Senior price")
else:
    print("Regular price")