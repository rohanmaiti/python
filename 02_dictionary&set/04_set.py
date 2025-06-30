# There are several ways to join two or more sets in Python.
# The union() and update() methods joins all items from both sets.
# The intersection() method keeps ONLY the duplicates.
# The difference() method keeps the items from the first set that are not in the other set(s).
# The symmetric_difference() method keeps all items EXCEPT the duplicates.


#* UNION |
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

#* You can use the | operator instead of the union() method, and you will get the same result.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)

#* can union multiple sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena", 3}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)
#* OR
myset = set1 | set2 | set3 | set4
print(myset)

#* Note: The  | operator only allows you to join sets with sets,
#* and not with other data types like you can with the  union() method.
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)

#* Update
# The update() method inserts all items from one set into another.
# The update() changes the original set, and does not return a new set.
x = {"a", "b", "c"}
x.update(('new value-1', 'new value-2'))
print(x)

#* Intersection
#* Keep ONLY the duplicates
#* The intersection() method will return a new set, that only contains the items that are present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

#* You can use the & operator instead of the intersection() method
set3 = set1 & set2
print(set3)
#* Note: The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.
#* The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.

set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1 & set2
print(set3)