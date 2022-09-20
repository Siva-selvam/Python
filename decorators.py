"""
Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behaviour of 
function or class. Decorators allow us to wrap another function in order to extend the behaviour of the wrapped 
function, without permanently modifying it

"""
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")
#make_pretty() is a decorator below
pretty = make_pretty(ordinary)
print(pretty())

#--------------------------------------------
@make_pretty
def ordinary():
    print("I am ordinary")

#it is equivalent to below

def ordinary():
    print("I am ordinary")
ordinary = make_pretty(ordinary)
print(ordinary)
