#unordered,mutable, no duplicates
myset = {1,2,3,2,1}
print(myset)

myset2 = set([1,2,3,4,2,2,2])  #convert lost to set
print(myset2)

st = set("nellllo")
print(st)

#to add the empty set use set(), if we directly give {} it takes it as dictionary
si = {}
si2 = set()
print(type(si))
print(type(si2))

#updating values
ex = {1,2,3}
ex.add(5)
ex.remove(1)
ex.discard(6) #if it is present then remove orelse it do nothing
print(ex)
ex.clear()

#set theory
odd = {1,3,5,7,9}
even = {2,4,6,8}
prime = {2,3,7}

u = odd.union(even)
i = odd.intersection(prime)
print(u,i)

diff = odd.difference(prime) #returns the elements only in the first set
print(diff)

rdiff = odd.symmetric_difference(prime) #returns the unique elements in both the sets
print(rdiff)

#updating the elemnts in the set

diff.update(rdiff)  #need to update the particular set directly otherwise it wont work
print(diff)

diff.intersection_update(rdiff) #only same element in both the set to be updated
print(diff)

diff.difference_update(rdiff) #only different element in both the set is updated
print(diff)

print(diff.issubset(rdiff)) #to check if all the element is present in the another set
#same like we have issuperset

set1 = set([1,2,3,4,5,6,5,6])
#set1 = set2 #we need to use copy() or set(set2) otherwise if we do changes it will overwrite it
#create immutabelset
a = frozenset([1,2,3,4,5,6])
print(a)