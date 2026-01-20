x = 5

def print_program_intro():
    print("DIVIDER 9000")
    print("v0.0.1")
    print("copyright 2026")

def divide(dividend, divsor):
    q = dividend//divsor
    r = dividend%divsor
    return (q,r)

if __name__ == "__main__":
    print_program_intro()
    num1 = float(input(">"))
    num2 = float(input(">"))
    print(divide(num1, num2))