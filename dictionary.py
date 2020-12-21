# Dictionary: key-value pairs, Unordered, Mutable
myDict = {"name":"Siddhesh","Age":19,"City":"Mumbai"}
print(myDict,"\n")

mydict2 = dict(name="Siddhesh",age=19,city="Mumbai")
print(mydict2,"\n")

""" Acessing the values of dictionary.
"""
value = mydict2["age"]
print(value,"\n")

""" NOTE: If we want to access an element which
is not present in the dictionary, we get an error i.e.'TypeError: 'dict' object is not callable'. 
"""

""" value = mydict2("Centre")
print(value,"\n")
"""

""" If we want to add a key-value pair in the dictionary.
"""
mydict2["email_id"] = "sid@xyz.com"
print(mydict2,"\n")

""" If we give another value to the key which already has 
a value, the value gets overwritten and the new value gets 
updated for that key.
"""
mydict2["email_id"] = "Coolsid@qwe.com"
print(mydict2,"\n")

""" To delete an item from Dictionary we have options:
        1] 'del' keyword method.
        2] pop() method.
        3] popitem() method.
"""

# OPTION 1 ['del' keyword method]
del mydict2["email_id"]
print(mydict2,"\n")

# OPTION 2 [pop() method]
mydict2.pop("age")
print(mydict2,"\n")

# OPTION 3 [popitem() method]
mydict2.popitem()
print(mydict2,"\n")
""" NOTE: In popitem() method removes the last
item of the Dictionary.
"""

""" If we want to check if the key is there in the dictionary,
    there are two ways to that:
        1] if else method
        2] try, except statement.
"""

# OPTION 1 [if else method]

if "name" in myDict:
    print(myDict["name"]," is present in the dictionary\n")
else:
    print("Not present in the dictionary\n")

# OPTION 2 [try, except statement]

try:
    print(myDict["name"],"\n")
except:
    print("Error\n")

""" If we want to loop through the dictionary,
    we have several methods:
        1] for loop.
        2] for loop with .keys() method(to get the keys only).
        3] for loop with .values() method(to get the values of the keys only).
        4] for loop with .items() method(to get both keys and values of the dictionary).
"""

# OPTION 1 [for loop]

for key in myDict:
    print(key,"\n")

# OPTION 2 [for loop with .keys() method]

for key in myDict.keys():
    print(key,"\n")

# OPTION 3 [for loop with .values() method]

for value in myDict.values():
    print(value,"\n")

# OPTION 4 [for loop with .items() method]

for key, value in myDict.items():
    print(key, value,"\n")

""" To copy a dictionary.
    There are 2 methods:
        1] '=' operator.
        2] use 'dict' keyword method.
"""

# OPTION 1 ['=' operator]

myDict_cpy = myDict
print(myDict_cpy,"\n")

""" NOTE: If we modify the copy it will modify the original one too.
"""
myDict_cpy["name"] = "Shankar"
print(myDict,"\n") 

""" If we want to avoid the above situation, we can use .copy() method.
"""
dict1 = {"name": "Siddhesh","Age": 19,"City": "Mumbai"}

mydict_cpy1 = dict1.copy()
mydict_cpy1["name"] = "Lionel Andres Messi"
print("Copied one: ",mydict_cpy1,"\n")
print("Original one: ",dict1,"\n")

# OPTION 2 ['dict' keyword method] 

dict_cpy = dict(dict1)
print(dict_cpy,"\n")

""" MERGING 2 dictionaries. 
"""
dict2 = {"name": "Max", "age": 19 , "email":"max@xyz.com"}
dict3 = {"name": "Siddhesh", "age": 27, "city":"Vancouver"}

dict3.update(dict2)
print(dict3,"\n")

""" Tuple in the Dictionary. 
"""
dict5 = {2:4, 3:9, 4:16, 5:25}
mytuple = (8,7)
dict5 = {mytuple: 15}
print(dict5,"\n")

""" NOTE: Only immutuable types are allowed to be there in dictionary.
    Otherwise, we will have an error: 'TypeError: unhasable type: 'list'. ' 
"""


