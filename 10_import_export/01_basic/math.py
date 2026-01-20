
# can export this 
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def print_hello():
    print("Hello...")
    __private_method()

# What actually gets “exported”?
# Everything in the module except names starting with _

def __private_method():
    """  """
    return print("this is a private method")
