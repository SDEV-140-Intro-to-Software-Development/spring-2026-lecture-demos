import os

def load_save_data():
    saveFile = open(os.path.join("2026-2-17-lecture-11", "save-data.txt"))
    lines = saveFile.readlines()
    saveFile.close()
    saveData = {}

    for line in lines:
        tokens = line.split("=")
        saveData[tokens[0]] = int(tokens[1])

    return saveData

def write_save_data(data):
    saveFile = open(os.path.join("2026-2-17-lecture-11", "save-data.txt"), "w")
    for key,value in data.items():
        saveFile.write(f"{key}={value}\n")

    saveFile.close()

print("loading save data")
data = load_save_data()
print(data)

print("changing values")
data['x'] += 1000
data['currency'] += 10

print("saving data")
write_save_data(data)

# set player pos to saved pos
# set player current to save currency