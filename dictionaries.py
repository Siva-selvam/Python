#key value pair, unordered, mutable
mydict = {"name":"siva", "age":28, "city":"newyork"}
print(mydict)

mydict2 = dict(name="mary", age=46)
print(mydict2)

#accesing
value = mydict["age"]
print(value)

#add or crate new key value pair
mydict2["email"] = "sivaselvamhak@gmail.com"
print(mydict2)

del mydict["name"]
print(mydict)

#remove the last item of the dict using popitem
mydict2.popitem()
print(mydict2)

#method 1
for key in mydict2:
    print(key)
#method2
for key in mydict2.keys():
    print(key)

#values
for value in mydict2.values():
    print(value)

#accesing both key and values
for key, value in mydict2.items():
    print(key, value)

#need to use copy() otherwise it will overwrite the original one as well
my1 = {"name":"siv","age":9,"like":"gasper"}
my2 = my1.copy()    #if we didnt give copy(), it will overwrite the existing dic as well
my2["king"] = "tarantino"
print(my1)
print(my2)

#updaate is like overwriting a dict with new values
dict1 = {"1":"number", "2":"two","3":"next", "ag":"77"}
dict2 = dict(name="siva", age=20, ag="iou")
dict1.update(dict2)
print(dict1)

#we can use numbers also as the key value pair
pair1 = {1:3,2:5,4:5,5:7}
print(pair1)

#we can sue tuple as the key, because it is immutable, we cant use list as the key becuase its mutable
tup=(1,2)
mydi = {tup:3}
print(mydi)