# #* Lamda function is function like arrow smallest arrow function syntax in js
#* A lamda function can take any number of arguments but only have one expression 

#* Syntax--> lambda arguments : expression
myFunction = lambda arg1, arg2, arg3 : arg1 + arg2 + arg3
print(myFunction(10,20,30))


#* like clouser in js this is the example of clouser in python
def function(num):
    return lambda arg : arg * num

myFunction = function(10)
print(myFunction(20))
