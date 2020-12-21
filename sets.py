# Sets: Unordered, mutable, no duplicates.

myset = {1,2,3,4,5,6}
print(myset,"\n")

""" NOTE: No duplicates in sets as always so if we have 
duplicates still only specific element will be shown. 
"""
myset = {1,2,3,4,5,6,1,2,1,2}
print(myset,"\n")

""" We can use set() function to create a set.
"""
myset1 = set("Hello")
print(myset1,"\n")
"""NOTE: The order of the set is arbitrary, unordered.
"""  

""" To create an empty set.
"""
myset2 = {}
print(type(myset2),"\n")
""" NOTE: The type will be a dicitonary for an empty set 
i.e. ' <class 'dict'> '.
    So to avoid this, we can use set() i.e. ' <class 'set'> '.
"""
myset2 = set()
print(type(myset2),"\n")

""" To add elements in the set.
"""
myset2.add(1)
myset2.add(2)
myset2.add(3)
print(myset2,"\n")

""" We can remove the elements from the set by .remove() method.  
"""
myset2.remove(1)
print(myset2,"\n")

""" NOTE: If we pass an element to be removed from the set but that element
is not there in the set, then it will show an error i.e. ' KeyError: 0 '.  

myset2.remove(0)
print(myset2,"\n")

"""
""" We can also remove/discard element from the set by using discard() method. 
"""
myset2.discard(2)
print(myset2,"\n")
""" NOTE: The best thing is that there will be no error produced if the 
element is not there in the set.  
"""

""" We can clear the set by using .clear() method. 
"""
set3 = {1,2,3,4,5,6,7,8,9,10}
set3.clear()
print(set3,"\n")

""" Since set is mutable, we can also use pop() fucntion.  
"""
myset2.pop()
print(myset2,"\n")

""" We can iterate through set.
""" 
for i in myset:
    print(i)

"""If we want to check whether an element is there in the set?
"""    
if 2 in myset:
    print("Yes ",2," is there in the set\n")
else:
    print("No it is not there!!\n")

""" UNION AND INTERSECTION in sets. 
"""
evens = {0,2,4,6,8,10}
odds = {1,3,5,7,9,11}
primes = {2,3,5,7,11,13}

union = odds.union(evens)
print(union,"\n")

intersection = odds.intersection(evens)
print(intersection,"\n")

""" DIFFERENCE in sets. 
"""
diff = evens.difference(odds)
print(diff,"\n")

""" SYMMETRIC DIFFERENCE in set 
"""
symdiff = evens.symmetric_difference(odds)
print(symdiff,"\n")

"""NOTE: Union, Intersection, difference and Symmetric difference don't
update the elements in a set.
"""

""" To update the set we use update().
"""
primes.update(evens)
print(primes,"\n")

""" Sub-set, Super-set and Disjoint sets. 
"""
setA = {1,2,3,4,5,6}
setB = {1,2,3}
# Sub-set
print(setA.issubset(setB),"\n")
# Super-set
print(setA.issuperset(setB),"\n")
# Disjoint set
print(setA.isdisjoint(setB),"\n")

""" COPYING SETS. 
"""
setB = setA
print(setB,"\n")
""" NOTE: With '=' operator it only changes the original one too.
"""
setB.add(9)
print("Copied one: ",setB,"\n")
print("Original one: ",setA,"\n")

""" To avoid this by using .copy() method.
"""
setC = setA.copy()
setC.add(7)
print("Original one: ",setA,"\n")
print("Copied one: ",setC,"\n")

""" FROZEN SET(immutable set). 
"""
a = frozenset({1,2,3,4})
print(a,"\n")
"""NOTE: All the methods which updates or changes the set contents won't work.
Only intersection, Union, Difference, Symmetric Difference works. 
"""