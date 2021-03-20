while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again...")
#------------------------------------------------------------------------------------
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')
#-------------------------------------------------------------------------------------
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

print(divide(2, 4))