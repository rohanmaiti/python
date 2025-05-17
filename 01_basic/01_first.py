# #*print some thing 
# print("Hello Rohan");
# # print varients
# print("My name is Rohan.");
# print("My age is 21");
# print("My name is Rohan.", "My age is 21.");

# #*printing number
# print(25);
# print(25+35);

# #*variable 
# name = "Rohan"; # string
# age = 21; # number 
# price = 15.23;
# print(name, age, price);
# print("my name is :",name);
name

# age2 = age; # copying the value
# print(age2);
# age = 23;
# print(age);
# print(age2);

# print(type(age));
# print(type(price));
# print(type(name));

# Datatype
# Integer, String (can be writen inside "str",'str','''str'''), Float, Boolean(True, Flase : note T and F are capital), None (None)
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

# Operator
# Arithmetic Operator
# a = 5
# b = 2
# print(a+b);
# print(a-b);
# print(a*b);
# print(a/b); # will give float value
# print(a%b);
# print(a**b);

# Relational Operator
# print(a == b);
# print(a != b);

# logical operator 
# print(not False);
# print(not (a>b));

# print(True and False)
# print((1 and 5));
# print((a == b) or (b > a));

# Type conversion
# 1. Type conversion (automatic)
# 2. Type casting (manully)

# a = "1.2";
# b = 5;
# sum = a + b; # error
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

# taking input
# name = input("enter your name : "); # take space also
# print("your name is :",name);
# print(type(name)); # all input value is bydefault string

# taking int as a input 
# num1 = int(input("Enter 1st number : "));
# num2 = int(input("Enter 2nd numner : "));
# print("Sum of two number is ", num1+num2);

# safe side to take input as number
# num1 = float(input("Enter float num1 : "));
# num2 = float(input("Enter float num2 : "));
# print("Sum of two number is ", num1+num2);


# question 
# take a input of a square and o/p the area
# side = float(input("enter side of a square: "));
# print("Area of square is ,",(side**2));