# Sort list of words in abc order

print("Enter list of words seperated by spaces")
user_input = input("> ")
word_tokens = user_input.split(" ")
word_tokens.sort()

print(word_tokens)
