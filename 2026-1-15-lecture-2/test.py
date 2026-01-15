
while 1:
    line = input(">>> ")
    pieces = line.split(" ")

    if pieces[0] == "ADD":
        num1 = float(pieces[1])
        num2 = float(pieces[2])
        print(num1 + num2)
    elif pieces[0] == "EXIT":
        exit()
    else:
        print("UNKNOWN OP")
        print("EXITING")
