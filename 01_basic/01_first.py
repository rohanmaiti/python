# #*print some thing 
# print("Hello Rohan");
# # print varients
# print("My name is Rohan.");
# print("My age is 21");
# print("My name is Rohan.", "My age is 21.");

# #*printing number
# print(25)
# print(25+35)
# name="Rohan"
# print(f"hii hello {name}")

# #*variable 
# name = "Rohan"; # string
# age = 21; # number 
# price = 15.23;
# print(name, age, price);
# print("my name is :",name);

# #* can not have a uninitilised variable like this
# fullname;  #* ERROR as not initialised
# #* make it initialise with None
# fullname = None;  #* in this case not error

# age2 = age; #* copying the value
# print(age2);
# age = 23;
# print(age);
# print(age2);

# *checking type
# print(type(age));
# print(type(price));
# print(type(name));

# #* Datatype in python
# #* Integer(int), String(str) (can be writen inside "str",'str','''str'''), Float(float), Boolean(True, Flase : note T and F are capital), None (None)
# x = True;
# a = None;
# print(type(x));
# print(type(a));
# c; #error as not defined
# print(c);
# print(type(c));


""" 
multiline comment 
"""

# #* Operator
# #* Arithmetic Operator
# a = 5
# b = 2
# print(a+b);
# print(a-b);
# print(a*b);
# print(a/b); #* will give float value
# print(a%b);
# print(a**b);

# #* logical operator (or, and, not)
# print(not False);
# print(not (a>b));

# print(True and False)
# print((0 and 5)); #* if any number is 0 and the operator is and them it returns 0 else returns the right side's number
# print(5 and 3); #* will return 3;
# print((5 or 0));
# print(4 or 3);  #* if both the numbers are not non-zero and the operator is or then retuns the left side's number
# print( 5 and 4 and 6 and 2);  #* will return the left most
# print((a == b) or (b > a));
# print ( a != b)

# *Type conversion
# *1. Type conversion (automatic)
# *2. Type casting (manully)  --> SYNTAX: DataType(ele)

# a = "1.2";
# b = 5;
# sum = a + b; #* error cause can only concatinate string unlike js where string + anything = string 
# print(sum);

# a = 1;
# b = "2.22";
# sum = a + float(b);
# print(sum);

# a = 1;
# b = "2.22";
# sum = a + int(float(b));
# print(sum);

# print(str(a));
# print(type(str(a)))

# #* taking input
# name = input("enter your name : "); #* take space also and all input are by default string
# print("your name is :",name);
# print(type(name)); #* all input value is bydefault string

# #* taking int as a input 
# num1 = int(input("Enter 1st number : "));
# num2 = int(input("Enter 2nd numner : "));
# print("Sum of two number is ", num1+num2);

# #* safe side to take input as number
# num1 = float(input("Enter float num1 : "));
# num2 = float(input("Enter float num2 : "));
# print("Sum of two number is ", num1+num2);


# #* question 
# take a input of a square and o/p the area
# side = float(input("enter side of a square: "));
# print("Area of square is ,",(side**2));

# #* question 
result = 10 / 3
print(result) # 3.33333333

#* to decide precidence 
result = round(10/3 , 2)
print(result)