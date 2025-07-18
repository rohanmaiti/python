

# make a decorator that print the name and the arguments of functions 

def debug(func):
    def wrapper(*args, **kwargs):
        print("Tuple argumets are ", *args)
        print("Dictonary arguments are ", **kwargs)
        return func(*args, **kwargs)   
    return wrapper


# ***
@debug
def greet(name, greeting='Hello'):
    print(f"{greeting} {name}")

@debug
def hello():
    print("hello from function hello")

greet("Rohan", "Namste")
hello()

