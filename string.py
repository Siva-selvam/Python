#ordered, immutable, text representation

my_string = "siva roro"
char = my_string[3]
print(char)

#strip() to remove leading trailing spaces
#upper() #lower()
#startswith #endswith
#find("e") #retunes first index
#count() retunes count
#replace
#split("delimeter") - split and place it in array
my_String1 = "hi,hello,how,are,you"
list1 = my_String1.split(",")
ls = " ".join(list1)
print(ls)    #join will convert from list to value based on delimiter

var = "tom"
name1 = "var is %s" %var   #placeholder %s - string %d -decimal %f - float
print(name1)

var2 = "va is {}" .format(var)
print(var2)

var3 = "va is {var}"
print(var3)