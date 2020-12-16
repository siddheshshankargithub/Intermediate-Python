# Lists = ordered, mutable, allows duplicate elements.

myList = ['banana','cherry','apple']
print(myList,"\n")

# a list can contain disimilar data elements too.

myList1 = ['siddhesh',12,10.101]
print(myList1,"\n")

# a list can contain duplicate elements.

""" NOTE: Even if the list can contain duplicate elements it still
shows them differently as if they are different elements.
"""
l = ['siddhesh',19070122168,'siddhesh']
print(l,"\n")

""" To access the elements in the list we have
have to use indexing method.
"""
result = l[2]
print(result,"\n")

""" NOTE: Always the index is (n-1), 
i.e. [ size of the list s - 1 ]
So the 1st element is at index '0' and the second element
at index '1'. 
"""
""" To iterate through the list we have two methods:
        1] By using the for loop.
        2] By using slicing method by using ':' operator.
"""
# 1st method
for i in myList1:
    print(i)

# 2nd method
x = myList1[1:2]
print(x,"\n")

""" OPERATIONS WITH LISTS """

myList3 = ["siddhesh","shankar",231111,"Hey"]

""" To check how many elements are there in my list:
"""
print(len(myList3),"\n")

""" To append something i.e. to add some element
in the end of the list.
"""
myList3.append("Hi")
print(myList3,"\n")

"""What is we want to add at a specific index of my choice?
"""
myList3.insert(2,"Blueberry")
print(myList3,"\n")

""" To remove the last element of the list
    We have two methods:
        1] pop() { removes the last element}
        2] remove() {removes the specified element}
"""
# 1st method
y = myList3.pop()
print(y,"\n")

# 2nd method

z = myList3.remove("Hey")
print(myList3,"\n")   

""" NOTE: if we give the element which is 
not there in the list while we use remove()
it will show an 'VALUE-ERROR'. 
"""
"""
h = myList3.remove("Penny")
print(h,"\n")
"""

""" To clear the list totally.
"""
list2 = [1,2,3,4,5,6,7,8,9,10] 
z = list2.clear()
print(list2,"\n")

""" To reverse the list we can use reverse() method.
"""
list3 = [111,21,1112,2211,44]
z = list3.reverse()
print(list3,"\n")

""" We can sort our list using sort() method.
"""
z = list3.sort()
print(list3,"\n")

"""If we want to sort a list into a new list, 
we use the sorted() method.
"""
new_list = sorted(list3)
print(new_list,"\n")

""" Suppose we want to create a list having 
duplicate elements like 5 zeroes. Then we can do:
"""
list4 = [0]*5
print(list4,"\n")

"""We can concatenate two lists using '+' operator.
"""
list5 = [1,2,3,4,5,6,7,8,9]
list6 = list3 + list5
print(list6,"\n")

""" Copying the list into an another list
by simply using '=' operator.
"""
list_org = ["Apple","Cherry","Banana","PineApple"]
list_cpy = list_org
print(list_cpy,"\n")
"""NOTE: If I make changes in copied list it will,
automatically change the original list too.
""" 
list_cpy.append("Orange")

print("COPIED ONE: ",list_cpy,"\n")
print("ORIGINAL ONE: ",list_org,"\n")
print("--------------------\n")

""" So to avoid this, we can use the copy()
method. 
"""
list_cpy1 = list_cpy.copy()
print("COPIED ONE: ",list_cpy1,"\n")
print("ORIGINAL ONE: ",list_cpy,"\n")

""" LIST COMPREHENSION: Fast & Elegant way to 
    copy the existing list.
"""
n = [1,2,3,4,5,6]
"""list_name = [op for i in org_list]"""
b = [i*i for i in n] 
print(b,"\n")


