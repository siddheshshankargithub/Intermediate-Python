# Tuple: ordered, immustable, allows duplicate elements.

myTuple = ("max",28,"Boston","Chicago")
print(myTuple,"\n")

"""If there is only one element in tuple, it will
show it's type is a string i.e."<class 'str'>". 
"""
tuple1 = ("Max")
print(type(tuple1))

# to correct it:
tuple1 = ("Max",)
print(type(tuple1))

""" Built-in tuple function:
"""
mytuple = tuple(["Siddhesh","Shankar",19])
print(mytuple,"\n")

"""Ascessing elements of tuple 
"""
item = mytuple[0]
x = mytuple[2]
print(item,"\n")
print(x,"\n")

""" NOTE: if we use index greater than the number
of elements in tuple, we get:'IndexError: tuple index out of range'.
"""
"""item = mytuple[5]
print(item,"\n")
"""

"""If we have change the elements like the list,
we get an error i.e. 'TypeError: 'tuple' object does not support item assignment'
"""
""" mytuple[0] = "Hi" 
"""

"""Iterate over the tuple with for loop.
"""
for i in mytuple:
    print(i)

""" To check whether an element is there in the tuple or not? 
"""    
if "Siddhesh" in mytuple:
    print("\n","Yes it is present\n")
else:
    print("\n","Not present\n")

""" To count the amount of duplicate element in the tuple
"""
tuple2 = ('a','b','c','d','e','b','b','b')
print(tuple2.count('b'),"\n")

"""To find the index of an element in tuple.
NOTE: Shows the first occurence only.
Also if the element is not there, then we get
ValueError.
"""
print(tuple2.index('b'),"\n")

"""To convert list to tuple and vice-versa. 
"""
my_list = list(tuple2)
print(my_list,"\n")
my_tuple = tuple(my_list)
print(my_tuple,"\n")

""" Equality in tuples.
"""
my_tuplez = "Siddhesh",19,"Mumbai"
name, age, city = my_tuplez
print(name,"\n")
print(age,"\n")
print(city,"\n")

# another example
my_tuple4 = (0,1,2,3,4)
i1, *i2, i3 = my_tuple4
print(i1,"\n")
print(i3,"\n")
print(i2,"\n") # remaining elements become a list.

""" Note: Working woth tuple sometimes is efficient than lists,
if we are dealing with larger data sets.  
"""
import sys
my_list1 = [0,1,2,"hello",True]
my_tuple1 = (0,1,2,'hello',True)
print(sys.getsizeof(my_list1),"bytes","\n")
print(sys.getsizeof(my_tuple1),"bytes","\n")

"""To see how iterating through tuples is efficient than lists.
"""
import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number = 1000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number = 1000000))


