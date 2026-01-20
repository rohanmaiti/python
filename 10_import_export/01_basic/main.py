# #* Anything defined in a .py file is exportable by default

# #* Basic import -> import <filename>
# how to use imported things ? --> filename.function_name()
import math
print(math.add(10, 20))

# when you will be checking this and run this file a __pycache__ folder will be created

# #* Import specific things 
# syntax -> from <fileName> import <function_name1, function_name2, ...>
from math import print_hello
print_hello()

# #* Import with alias
from math import print_hello as ph
ph()

# #* Multiple imports
from math import add, sub, print_hello as ph

