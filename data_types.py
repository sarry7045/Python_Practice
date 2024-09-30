# Data Types or Object Types
# - Number :
# - String :
# - List : [1,2,3[4,5]]     list(range(10))
# - Tuple : (1, 'spam', 4, 'U')     nametuple
# - Dictionary : {'Food':"spam", 'taste':"yum"}     dict(hours=10)
# - Set : set('abc'), {'a', 'b', 'c'}
# - File : open('eggs.txt'), open(C:\ham.bin, "wb")
# - Boolean : 
# - None : None
# - Functions : module, classes

# -Advance : Decorators, Generaators, Iterators, MetaProgramming



import math
import random
print(math.pi)
print(random.random())
print(random.choice([1,2,3]))



usename = "Sarry"
print(len(usename))
print(usename[0])
print(usename[1:3])
# print(dir(usename))



# String is inMutable
# usename[0] = "A"   -   We can't change like this
# Ek baar object agar define ho gaya hai memory me toh, hum new object banake he reference de sakte hai, exsiting me change nhi hota



mylist = [123, "Code", 3.14]
print(len(mylist))
myListOne = [1,2,3]
myListTwo = myListOne
myListOne[0] = 33
# myListOne is now = [33,2,3]
# myListTwo is now = [33,2,3]
# List is Mutable



myTup = (1,2,3)
