words = []
user_input = input("> ")

while user_input != 'q':
    words.append(user_input)
    user_input = input("> ")

if len(words) > 0:
    for word in words:
        print(word)
else:
    print("No words")