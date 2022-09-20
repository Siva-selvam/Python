#ordered - sort , immutable, allows duplicsted as well

# tuples takes low space compared to list

mytup = ("max",28,"siv",28)
print(mytup)

mytup2 = ("max2",)
print(mytup2)

mytupl = tuple(["max", 2, "min"])
print(mytupl[0])

myt = ("a","b","c","d","a")
a=sorted(myt)
print(a)
print(len(myt))
print(myt.count("a")) #count occuranes of a
print(myt.index("c")) #returns index of first occurance

a = (1,2,3,4,5,6,7,8,9,0,10)
b=a[::-1]
print(b)

#assigning to variable
max = ("siva", 24, "stark")
peru, age, alias = max
print(peru)
print(age)
print(alias)

# using inbetween list creation
max1 = (1,2,3,4,5,6,7,8,9)
i1,*i2,i3 = max1
print(i1)
print(i2)
print(i3)
print("=================")
mr = range(6)
for i in mr:
    print(i)
