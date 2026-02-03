
user_input = input('> ')
loop_count = 0

while user_input != 'q':
    if loop_count > 5:
        break

    print(user_input)
    loop_count += 1

    user_input = input('> ')