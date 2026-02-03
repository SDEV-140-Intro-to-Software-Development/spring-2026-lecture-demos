grade = int(input("Grade level (0-12)? "))

if 9 <= grade <= 12:
	print("in high school")
else:
	print("not in high school")

# equivlant code
if grade >= 9 and grade <= 12:
	print("in high school")
else:
	print("not in high school")