# #* Dictionary in python | it is like object in javacript
# #* features--> 1. unorders 2. mutable 3.don't allow duplicate keys 4.key can be a number


# #* creating a dictionary 
# dic = {
#     "name" : "Rohan",
#     "age" : 21,
#     100 : 'number'
# }
# print(type(dic))

# #* printing the whole disctionary
# print(dic)

# #* Accessing a specific key
# print(dic["name"])
# print(dic[100])

# #* Accessing using get method
# print(dic.get("name"))

# #* Add items
# dic['another_key'] = 'new key'
# print(dic);
# #* Add items using update 
# dic.update({'newKey': 'newValue', 'newKey2': 'newValue2'})
# print(dic)



# #* if there is two key it will overwrite 
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# print(thisdict)

# #* length of dictionary as as list and tuple 
# print(len(thisdict))

# #* The values in dictionary items can be of any data type:
# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }

# print(thisdict['colors'][1])


# #* changing value in dic
# thisdict["brand"] = 'Nike'
# print(thisdict)

# #* The keys() method will return a list of all the keys in the dictionary.
# print(thisdict.keys())
# x = thisdict.keys()

# #* The values() method will return a list of all the values in the dictionary.
# print(thisdict.values())

# #* The items() method will return each item in a dictionary, as tuples in a list.
# print(thisdict.items())

# #* Check if Key Exists --> use the in keyword:
# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")

# #* Removing Items
# #* There are several methods to remove items from a dictionary:
# #* The pop() method removes the item with the specified key name:
# thisdict.pop('model')
# print(thisdict)

# #* The popitem() method removes the last inserted item
# thisdict.update({'model': 'maiti'})
# print(thisdict)
# thisdict.popitem()
# print(thisdict)

# #* The del keyword removes the item with the specified key name: just like JS
# del thisdict["brand"]
# print(thisdict)
# #* The del keyword can also delete the dictionary completely:
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict
# print(thisdict) #* this will cause an error because "thisdict" no longer exists.

# * The clear() method empties the dictionary:
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.clear()
# print(thisdict)


# * Loop Through a Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# * print all keys in the dictionary
for x in thisdict:
  print(x)

# * Print all values in the dictionary, one by one:
for x in thisdict:
 print(thisdict[x])


# #* You can also use the values() method to return values of a dictionary:
for x in thisdict.values():
  print(x)

# #* You can use the keys() method to return the keys of a dictionary:
for x in thisdict.keys():
  print(x)

# #* Loop through both keys and values, by using the items() method:
for x, y in thisdict.items():
 print(x, y)
