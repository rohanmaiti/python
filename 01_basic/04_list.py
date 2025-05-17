# #* LIST  (mutable) (heterogenous)
# marks = [1,2,3,4,5,6,7,"Rohan"];
# print(marks);
# print(type(marks));

# print(marks[0]);
# print(marks[len(marks)-1]); #* length of List

# marks[0] = "100"; #* can assign value using index unlike string
#                   #* string are immutable in python
# print(marks);

# #* slicing is also same here
# print(marks[1:4]);
# print(marks[-3:-1]);

# #* Function : print, len
# #* Methods : for specific ex- list methods
# list = [2,1,3];
# list.append(4);
# print(list.append(5)); # change in original string and return None
# print(list);

# #* sorting
# list.sort(); # sorting in assending order # change in original string and return None
# print(list);

# list.sort(reverse=True); #* sort in reverse order
# print(list);

# #* sorting for string also --> lexilogically
# list =["rohan", "rahul", "orange"];
# list.sort();
# print(list);

# #* for sorting have, the list have to be homogenous
# list=[1,2,4.5,3,6]; # work as all are number
# list.sort();
# print(list);

# but
# list = ["rohan",12,4,"Kalu"];
# list.sort(); # error


# #* reverse a list
# list = [1,2,3,4,5];
# list.reverse();
# print(list);

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