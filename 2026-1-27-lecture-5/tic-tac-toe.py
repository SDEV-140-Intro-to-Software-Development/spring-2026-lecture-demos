tic_tac_toe = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def print_board():
    for y, row in enumerate(tic_tac_toe):
        for x, element in enumerate(row):
            if x == len(row) - 1:
                print(element, end="\n")
            else:
                print(element, end=" | ")

        if y != len(tic_tac_toe) - 1:
            print("------------")

current_player = 'X'
while True:
    print_board()
    print("Where would you like to go? (1-3) Ex: 2 3")
    user_input = input("> ")
    coordinates = user_input.split()
    coordinates[0] = int(coordinates[0]) - 1
    coordinates[1] = int(coordinates[1]) - 1

    tic_tac_toe[coordinates[1]][coordinates[0]] = current_player

    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'
