from datetime import datetime
import os

def log(text):
    f = open(os.path.join("2026-2-17-lecture-11", "log.txt"), "a")
    f.write(f"{datetime.now()}: {text}\n")

while True:
    user_input = input(">")
    try:
        value = int(user_input)
        print(value)
        if value == -1:
            break
    except:
        log(f"{user_input} is not a valid number!")
