# #* LIST  (mutable) -> means changeable, (heterogenous) -> means can store multiple dt at once

# * creating and accessing Lists
# arr = [1, 2, 3, 4]
# print(arr[0])  # Access first element

# * empty list
arr = []

# * ADDING ELEMENT IN LIST
# arr.append(10)
# arr.append(20) # Add at end
# print(arr)

# arr.insert(1, 10)    # Insert 10 at index 1
# arr.extend([6, 7])   # Add multiple elements ( can be a tuple as well )
# print(arr)

# * LENGTH OF LIST
# print(len(arr))

# * REMOVING ELEMENT FROM LIST
# arr.remove(10)  #* Remove first occurrence of 10
# print(arr)

# item = arr.pop()  #* Remove last element also return return it
# print(item)
# print(arr)

# item = arr.pop(2)  #* Remove item at index 2  also return the poped element
# print(item)
# print(arr)

# del arr[0]  # Delete element at index 0 but do not return poped item
# arr.clear()  # Remove all elements

# marks[0] = "100"; #* can assign value using index unlike string
#                   #* string are immutable in python
# print(marks);

# #* SLICING 
# print(marks[1:4]);
# print(marks[-3:-1]);

# #* Function : print, len
# #* Methods : for specific ex- list methods
# list = [2,1,3];
# list.append(4);
# print(list.append(5)); # change in original string and return None
# print(list);

# #* SORTING 
# list.sort(); # sorting in assending order # change in original string and return None
# print(list);
# list.sort(reverse=True); #* sort in reverse order
# print(list);


# #* sorting for string also --> lexilogically
# list =["rohan", "rahul", "orange"];
# list.sort();
# print(list);

# #* for sorting, the list has to be homogenous
# list=[1,2,4.5,3,6]; # work as all are number
# list.sort();
# print(list);

# but
# list = ["rohan",12,4,"Kalu"];
# list.sort(); # error


# #* REVERSE
# arr = [1, 2, 3, 4]
# arr.reverse()
# print(arr)


# #* insert at index
# list = [1,2,3,4,5];
# list.insert(1, 500); #* can insert one ele at a time
# print(list);

# #* remove element from list
# list = [2,1,3,1];
# list.remove(1); #* remove(ele) --> removes first occurance of the element

# #* pop(idx)
# list = [0,1,2,3,4,5,6,7,8,9];
# list.pop(2);
# print(list);


# #* SEARCHING 
arr = [1, 2, 3, 2]
print(arr.index(2))  # First index of 2
print(3 in arr)      # Check if 3 is in list
print(arr.count(2))  # Count occurrences of 2