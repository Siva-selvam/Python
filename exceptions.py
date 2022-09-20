while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again...")
#------------------------------------------------------------------------------------
try:
    a=5/0
except Exception as e:
    print(e)
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

#--------------------------------------------------------------------------------------
# minimal example for own exception class
class ValueTooHighError(Exception):
    pass
# or add some more information for handlers
class ValueTooLowError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(a):
    if a > 1000:
        raise ValueTooHighError('Value is too high.')
    if a < 5:
        raise ValueTooLowError('Value is too low.', a)
    return a
try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooLowError as e:
    print(e.message, 'The value is:', e.value)