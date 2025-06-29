# #* Copy a Dictionary
# #* You cannot copy a dictionary simply by typing dict2 = dict1, 
# #* because: dict2 will only be a reference to dict1, 
# #* and changes made in dict1 will automatically also be made in dict2.

# *There are ways to make a copy, one way is to use the built-in Dictionary method copy().
# obj = {
#     'name': 'Rohan',
#     'age' : 21,
#     'stream' : 'CSE'
# }
# obj2 = obj
# obj2['name'] = 'rahul'
# print(obj)
# print(obj2)

# obj3 = obj.copy()
# obj3['name'] = 'Tamanna'
# print(obj)
# print(obj3)

# #* Another way to make a copy is to use the built-in function dict().
# obj4 = dict(obj)
# obj4['name'] = 'Raj'
# print(obj)
# print(obj4)


# #* Neasted Objects
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# #* Access Items in Nested Dictionaries
print(myfamily['child2']['name'])

# #* Loop Through Nested Dictionaries

for key, obj in myfamily.items():
    for innerKey in obj:
        print(obj[innerKey]);