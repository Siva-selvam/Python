"""List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members."""
#ordered, mutable, allows duplicate
mylist = ["banana","mango"]
print(mylist)

#empty list
mylist1 = list()
print(mylist1)

#all the possible values
mylist2 = [5, True, "siva",5]
for i in mylist2:
    print(i)

if 5 in mylist2:
    print("yes")
else:
    print("No")
mylist2.append(False)
print(mylist2)
mylist2.insert(1,"me")
print(mylist2)

#pop
mylist2.pop()
print(mylist2)  #removes he last occurance value inthe list
item=mylist2.pop()
print(mylist2) #even if we assign to the seperate variable also, it will do pop yo the list

#remove
mylist2.remove(5)
print(mylist2)

mylist.append("siv")

mylist2.reverse()
print(mylist2)

#clear
mylist.clear()

#sort and sorted
list = [1,12,3,4,5]
list.sort()  #directly modify the original list like override it
print(list)
list = [1,12,3,4,5,11,7,9]
list1 = sorted(list)   #sort seperatly and doesnt overwrite the original list
print(list1)
print(list)

#list edition
list3 = [1] * 5
print(list3)

list4 = list3 + list
print(list4)

#slicing
print(list4[1:5])
print(list4[:8:2])
print(list4[:-1:2])
print(list4[::-1])    #the second colon indicates the step index

#copy
list5 = list4.copy()   #it doesnt overwrite the source variable
list5.append(9)
print(list5)
print(list4)

list5 = list4[:3]    #slicing also do the same doesnt overwrite it
print(list5)
print(list4)

listend = ["siva",1,True,"is","worst","but","."]   #for printing all the values inside the list
print(*listend, sep="\n")