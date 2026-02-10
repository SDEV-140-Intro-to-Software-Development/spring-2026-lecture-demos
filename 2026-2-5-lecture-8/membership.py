colors = ["red", "green", "blue"]

user_input = "Red"

user_input = user_input.strip().lower()

print(user_input in colors)
print("purple" in colors)
print("purple" not in colors)


channels = {"CNN": 28, "NBC": 4}

print("CNN" in channels)   # True (key exists)
print(28 in channels)      # False (NOT checking values)
print(28 in channels.values())  # True