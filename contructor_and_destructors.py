#constructor initialises automatically when we create object of class
#destructor: when there is no need of object anymore in program it will destruct it to save memory

class Date:
    def __init__(self, year, month, day): #constructor
        self.day = day
        self.month = month
        self.year = year

    """
    In Python, the @classmethod decorator is used to declare a method in the class as a class method 
    that can be called using ClassName.MethodName() . The class method can also be called using an object 
    of the class
    """

    @classmethod
    def day(cls, day, month, year): #day-month-year
        cls.year = year
        cls.month = month
        cls.day = day
        return cls(cls.year, cls.month, cls.day)
    #order of return should be some as init  
    @classmethod
    def mdy(cls, month, day, year):
        cls.month = month
        cls.year = year
        cls.day = day
    #order of return should be some as init
        return cls(cls.year, cls.month, cls.day)

    def __del__(self):    #destructor
        print("objects are deleted")

a=Date(2016, 12, 11)
print(a.year) #2016
b=Date.day(9, 10, 2015)
print(b.year)
a=Date.mdy(7, 8, 2014)
print(a.year) #2014