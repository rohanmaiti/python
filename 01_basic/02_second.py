# #* STRING(immutable) ( \n:for next line, \t: for tabspace)
# str1 = "This is a string. \nAnd this is next line and a tab \tabc"
# print(str1);

# #* concatinaiton
# str1 = "string 1";
# str2 = "string 2";
# print(str1+str2);

# #* lenght of a function
# print(len(str1));

# #* indexing
# print(str1[0], str1[1], str1[2]);
# #* but can't change using index
# # str1[0] = "X"; # X
# # print(str1);

# #* slicing
# str="01234567"
# print(str[1:4]);
# print(str[2:len(str)]);
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

