caffeine_content = {
    "coffee": 90,
    "tea": 47,
    "sode": 40,
    "energy drink": 80
}

# print("What would you like to know the caffine value of?")
# user_query = input(">")

# if not user_query in caffeine_content:
#     print(f"Could not find caffine content for: \"{user_query}\"coke. Please try something else")
# else:
#     value = caffeine_content[user_query]
#     print(f"Caffine Content of {user_query} is {value}mg")

print("What beverage would you like to add?")
beverage = input("> ")
print("What is the caffeine content?")
beverage_caffeine_content_mg = input("> ")

if not beverage_caffeine_content_mg.isnumeric():
    print("ERROR: You must enter a number for caffine content!!!")
    exit(1)

if beverage in caffeine_content:
    print(f"ERROR: \"{beverage}\" already exist in data set!")

caffeine_content[beverage] = int(beverage_caffeine_content_mg)

print(caffeine_content)