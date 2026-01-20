# #*  In Python a function is defined using the def keyword:

def sum(num1, num2):
    print(num1 + num2)

# calling the function 
sum(10, 30)

# #* Positional arguments
def my_function(arg1, arg2):
    print('printing arguments', arg1, arg2)

my_function('rohan','rahul')
# what if i am passing one parameter in a 2 argument functoin ?
# my_function('kanu')  # it will throw error , if if want to make some argument as optional then will have to assign that with None

def my_function(arg1, arg2=None):
    print(f"printing arguments {arg1} and {arg2}")

my_function('rohan')

# #* Keyword arguments
def my_function(a, b):
    print(f"Printing a={a} b={b}")

my_function(b=10, a=20)

#* Arbitrary Arguments, *args
def my_function(name, *marks):
    print('name of the student is', name)
    print('marks of the student is', marks)
my_function('Rohan', 10,20,30,40)

# like js can have same function name, it will overwrite the function defination 

#*  can also send arguments with the key = value syntax.
#*  This way the order of the arguments does not matter.
def my_function(key1, key2, key3):
    print('printing the arguments', key1, key2, key3)

my_function(key3='3rd argument', key1='1st argument', key2='2nd argument')

#* Arbitrary Keyword Arguments, **kwargs
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Rohan", lname = "Maiti")

#* Default Parameter Value
def my_function(fname, lname, country_code='+91'):
    print('Name of the person is', fname, lname, 'and the his country code is', country_code)

my_function('Rohan','Maiti')
my_function('Rahul','Maiti', '+1')

#* passing list as a arguments
def my_function(list):
    print('printing the list....')
    for val in list:
        print(val)

list = [1,2,3,4,'abc',None]
my_function(list)

#* function returning the values
def operation(num1, num2=0):
    print('write logic here')
    return num1 * num2
print(operation(10, 20))

# #* Python function can return multiple values as tuple 
def my_function(a,b):
    return a+b, a-b

sum, sub = my_function(10, 5)
print(f"sum = {sum} and sub = {sub}")
