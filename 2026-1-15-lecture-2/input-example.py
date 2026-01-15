print("What is your hourly wage?")
wage = input("> ")

if not wage.isnumeric():
    print(f"{wage} is not a number!")
    exit()

wage = float(wage)

if wage <= 0.0:
    print(f"${wage} is too low, please find another job!")
    exit()

hours = 40
weeks = 52
 
salary = wage * hours * weeks
print(f"Salary is: {salary}")