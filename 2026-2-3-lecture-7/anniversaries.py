years = int(input("Years married? "))

if years == 1:
	print("Newlyweds")
elif years == 25:
	print("Silver")
elif years == 50:
	print("Golden")
# else:
# 	print("Congrats")

if years == 1:
	print("Newlyweds")

if years == 25 and years != 1:
	print("Silver")

if years == 50 and years != 25 and years != 1:
	print("Golden")