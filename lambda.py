#lambda arguments : expression
from functools import reduce
l = lambda x: x + 10
print(l(10))

def add_fun(x):      #same funciton with normal method
    return x + 10
print(add_fun(10))

l2 = lambda  x,y : x*y
print(l2(5,6))

points2D = [(2,3),(-3,1),(7,5),(9,2),(11,7)]
l3_sort = sorted(points2D,key=lambda x:x[0])  #sort based on index 1
print(l3_sort)

sorted_add = sorted(points2D, key= lambda x: x[0]+x[1])
print(sorted_add)

"""
map() function returns a map object(which is an iterator) of the results after applying the given function to each 
item of a given iterable (list, tuple etc.)
Syntax :
map(fun, iter)
"""
#map(func,seq)
a = [1,2,3,4,5,6]
b = list(map(lambda x:x*3,a))
print(b)

#list comprehension
c = [x*3 for x in a]
print(c)
"""
The filter() method filters the given sequence with the help of a function that tests each element 
in the sequence to be true or not.
syntax:
filter(function, sequence)"""
#filter(function, seq)
d = filter(lambda x:x%2==0,a)
print(list(d))
e = [x for x in a if x%2==0]
print(e)

"""
Python’s reduce() is a function that implements a mathematical technique called folding or reduction. 
reduce() is useful when you need to apply a function to an iterable and reduce it to a single cumulative value.
"""
v = [1,2,3,4]
product_a = reduce(lambda x,y:x*y, v) #its like a produt
print(product_a)

def my_add(a, b):
        result = a + b
        return result

numbers = [0, 1, 2, 3, 4]
print(reduce(my_add, numbers))
#0 + 1 = 1
#1 + 2 = 3
#3 + 3 = 6
#6 + 4 = 10
a : int = 6
print(a)

#reverse string
def balanced(expression):
    count = 0 
    for char in expression:
        if char == "(":
            count += 1
        elif char == ")":
            if count == 0:
                return False
            count -= 1 
    return count == 0

print(balanced(input()))

def reverse(string):
    string = string[::-1]
    return string
print(reverse("siva"))

def reverse1(string):
    string = "".join(reversed(string))
    return string
print(reverse1("sivas"))