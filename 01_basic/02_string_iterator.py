
#****** Mutable                         and                    Immutable 
# list, set, dictionary                            string, all number types, tuple, boolean
# #* STRING(immutable) ( \n:for next line, \t: for tabspace)
# str1 = "This is a string. \nAnd this is next line and a tab \tabc"
# print(str1);

# #* concatinaiton
# str1 = "string 1";
# str2 = "string 2";
# print(str1+str2);

# #* lenght of a string
# print(len(str1));

# #* indexing (0 base indexing)
# print(str1[0], str1[1], str1[2]);
# #* but can't change using index
# # str1[0] = "X"; # X
# # print(str1);

# #* slicing
# str="01234567"
# print(str[1:4]);
# print(str[2:len(str)]); #* 2 to last index
# print(str[2:]); #* 2 to last index
# print(str[:4]); #* 0 to 3 index
# print(str[5:1])

# #* nevative indexing as like js
# print(str[-3:-1]);

# #* string function 
# str = "i am coder and i am learing javam";
# print(str.endswith("er"));
# print(str.endswith("xer"));

# print(str.capitalize()); #* make the first character capital, if already capital then also keep it capital
# print(str); #* do not change in original string, return a new string as immutable

# print(str.replace("a","x")); #* replace all
# print(str); #* do not change in original string
# print(str.find("coder")); #* returns the staring index ofthe word else -1
# print(str.find("xoder")); #* returns the staring index ofthe word else -1

# print(str.count("am")) #* returns the number of time the word occurs

# #* Q. Input a user name and pritn its length
# name = input("Enter user name: ");
# print("Length of the username is: ",len(name));

# #* Q Count the number of occurance of $ in a string
# str = "i am a $coder and $ will go to school";
# print("Number of time $ appear in the string is", str.count("$"));

# #* join
# list = ['one', 'two', 'three']
#* how to make the list values print like this ---> one, two, three
# result = (', ').join(list)
# print(result)

# #* split
# string = 'rohan rahul tamanna'
# result = string.split(' ') #* returns list
# print(result)
# print(type(result))

#* Map || Comprehension
# Example-1 
# def square(n):
#     return n*2
# result = [square(x) for x in [1, 2, 3]] # this is like map--> at each iteration it returns something
# print(result)
# Example-2 (another syntax)
# result = [x*2 for x in [1,2,3]]
# print(result)

#* Ternary Operator 
# syntax -->#* <value_if_true> if [condition] else <value_if_false>
# result = "Number is even" if (10%2 == 0) else "Numbre is odd"
# print(result)

#* question-> loop through the array and return the number if it is even else return None
# result = [x if(x%2 == 0) else None for x in [1, 2, 3, 4, 5, 6, 7, 8]]
# print(result)

#* Filter
# result = [x for x in [1,2,3,4,5,6,7,8,9] if (x%2 == 0)]
# print(result)

#* some / every 
# result = any( x > 2 for x in [1,2,3,4,5]) #* returns True or False
# print(result)
# result = all( x > 2 for x in [1,2,3,4,5]) #* returns True or False
# print(result)
# print(type(result))
#* Array Merge / Concat
# concated_array = [1, 2] + [3, 4]
# print(concated_array)

#* SORT
result = sorted([3, 1, 4])  # [1, 3, 4] 
print(result)

#* spread operator 
array1 = [1,2,3,4,5,6]
array2 = [*array1, 7,8,9]
print(array2)


# ✅ 9. Zip (like JS Object.entries() & Object.fromEntries())
keys = ['name', 'age']
values = ['Rohan', 22]
dict(zip(keys, values))  # {'name': 'Rohan', 'age': 22}
