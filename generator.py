"""
A generator is a special type of function which does not return a single value, instead, 
it returns an iterator object with a sequence of values. In a generator function, 
a yield statement is used rather than a return statement.
"""

#iterable  is lst - just a collection of things which are able to iterate as iterable
lst=[1,2,3,4,5,6]
for i in lst:
    print(i)

iterator = iter(lst)   #iterator object
print(iterator)

try:
    print(next(iterator))    #each time it executes and it returns the values from iterators one by one
except StopIteration:
    print("its empty")

for i in iterator:   # we can directly use to iterate by using the object
   print(i)

#generators are always used to create an iterators
def square(n):
    for i in range(n):
        return i

square(4)   #it returns only the first iteration value

#now change the function to iterator
def square(n):
    for i in range(n):
        yield i**2

a=square(5)
print(a)
print(next(a))


#difference bt iterator and generator
"""
to create iterator we use iter keyword
to create generator we use function along with yield keyword
generator uses the yield keyword which save the local variable and it returns that
generator helps us to write fast and compact code
iterators are memory efficient

"""
import types, collections
print(issubclass(types.GeneratorType, collections.Iterator))