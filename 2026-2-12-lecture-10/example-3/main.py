import factorial.io
import factorial.math

num = None
for i in range(10):
    try:
        num = factorial.io.positive_int_input("Enter a number to get the factioral of: ")
        break  
    except ValueError as error:
        print(error)
        print("Please input a valid positive whole number!")
    except Exception as error:
        print(error)
        print("Uknown error occurred...")

if num == None:
    print("You failed to input a valid number too many times. Exiting...")
    exit()

factorial.io.print_factorial_equation(num)
print(factorial.math.factorial(num))