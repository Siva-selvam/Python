#itertools: product, permutations,combinations,accumulate, groupby and infinite iterations
from itertools import product
from itertools import permutations
from itertools import combinations, combinations_with_replacement
from itertools import accumulate
from itertools import groupby
from itertools import count, cycle, repeat
def smaller_than_3(x):
    return x<3
import operator
ac = [1,2,3,7,4]
a = [1,2]
b = [3,4]
prod = product(a,b) #repeat is another parameter we can add retunrs cartesian add
print(list(prod))  #if we give directly prod alone it shows like a itertools object
perm = permutations(ac)   #if we give permutations(ac,2) it retunrs 2 combinations
print(list(perm))
comb = combinations(ac,2)
print(list(comb))
comb_wr = combinations_with_replacement(ac,2)  #repeated manner
print(list(comb_wr))
accu = accumulate(ac)
print(list(accu))
accu_m = accumulate(ac, func=operator.mul) #accumulate by multiplying
print(list(accu_m))
accu_max = accumulate(ac, func=max)
print(list(accu_max))
ai = [1,2,3,4,5,6,7]
group_obj = groupby(ai, key=smaller_than_3) #or key as lambda x: x<3
#print(*group_obj,end="")
for key, value in group_obj:
    print(key, list(value))

person = [{'name': 'Tim','age':25}, {'name':'Dan','age':25},{'name':'siva','age':24}]
group_obj2 = groupby(person, key= lambda x: x['age'])
for key, value in group_obj2:
    print(key, list(value))
"""
for i in count(10):
    print(i)
    if i == 100:
        break
acy = [2,3,4,5]
#for i in cycle(acy):
 #   print(i)  #print continuosly acy values
#for i in repeat(1): #repear(1,4(repeats 4times of 1))
 #   print(i)"""