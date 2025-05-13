# list vs tuple
# tuple--> immutable data types
# list --> mutable data type

# tup = (2,1,3,4);
# print(tup);
# print(tup[0]);
# print(type(tup));

# tup[0] = 100; # error

# ean create empty tuple also can create empty list
# list = [];
# print(list);

# single value tuple writing systax
# tup = (1,);
# print(type(tup));

# why
# tup = (10);
# print(type(tup));

# sliceing also same here
# methods in tuple

# tup = (1,2,3,4,5,6,3);
# print(tup.index(3));  # tup.index(ele) ---> will return the first occarance index
# print(tup.count(3));

# Q. Ask to enter three movie names from user and store it in a list
# movie1 = input("Enter first movie name: ");
# movie2 = input("Enter second movie name: ");
# movie3 = input("Enter third movie name: ");
# list = [];
# list.append(movie1);
# list.append(movie2);
# list.append(movie3);
# print(list);
# Q. WAP to check if a list contains a palindrome of element
list = [1,2,3,4,3,2,1];
list2 = list.reverse();
if(list == list2):
    print("Palindrome");
else:
    print("Not pelindrome");