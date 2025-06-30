# #* Sets are used to store multiple items in a single variable.
#* Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, 
#* A set is a collection which is unordered, unchangeable*, and unindexed.
#*  Note: Set items are unchangeable, but you can remove items and add new items.

myset = { 'one', 'two', 'one'}
# print(myset)

#* Access Items
# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, 
for x in myset:
    print(x)

# The values True and 1 are considered the same value. The same goes for False and 0.
set = { 1, 3, 'number', True, False, 0}
print(set)


#* Check if "banana" is present in the set:
print('banana' in myset)
print('two' in myset)

#* Check if "banana" is NOT present in the set:
print('banana' not in myset)

#* Add items in set
myset.add('new data')
print(myset)

#* To add items from another set into the current set, use the update() method.
myset2 = {"apple", "banana", "cherry"}
myset.update(myset2)
print(myset)

#* Add Any Iterable in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

#* remove set items
thisset = {"apple", "banana", "cherry"}
# thisset.remove('abc') #* if removed item not present then it will throw error
thisset.remove('apple')
print(thisset)
#* Remove "banana" by using the discard() method:
thisset.discard("banana")
print(thisset)


#* You can also use the pop() method to remove an item, but this method will remove a random item,
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

#* The clear() method empties the set:
thisset.clear()
print(thisset)
thisset.clear() #* can clear empty sets also, no problem
print(thisset)