# if 1 person, seat a counter
# if 2 or more seat a table
# print out where we are seating the users

party_size = int(input("Party Size? "))
seat = None

if party_size < 1:
    print("invalid party size")
    exit(1)

if party_size == 1:
    seat = "Counter"
else:
    seat = "Table"

print(seat)