def load_save_data():
    saveFile = open("2026-2-17-lecture-11\save-data.txt")
    lines = saveFile.readlines()
    saveFile.close()
    saveData = {}

    for line in lines:
        tokens = line.split("=")
        saveData[tokens[0]] = int(tokens[1])

    return saveData


data = load_save_data()

# set player pos to saved pos
# set player current to save currency