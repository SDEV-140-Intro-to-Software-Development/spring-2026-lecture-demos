wall = {
    "x": 1,
    "y": 2,
    "width": 2,
    "height": 2
}

def is_player_in_wall(next_move):
    for y in range(wall['y'], wall['y'] + wall["height"]):
        for x in range(wall['x'], wall['x'] + wall["width"]):
            if next_move['x'] == x and next_move['y'] == y:
                return True

    return False


