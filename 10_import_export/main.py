# #* Option 1: Import whole module
# from utils import math_utils
# print(math_utils.PI)

# #* Option 2: Import specific functions/variables (like JS destructuring)
from utils.math_utils import add, PI
print(PI)

# #* Option 3: Import with alias
from utils import math_utils as mu
print(mu.PI)


# ✨ 3. Wildcard Import (⚠️ Not recommended)
from utils.math_utils import *
print(add(2, 3))  #


#* How make a directory as a package ?
"""
package is simply:
A folder containing Python files (modules)
A special file named __init__.py that tells Python “This folder is a package you can import from”.

ex-
my_package/
    __init__.py.    #This can be empty, or it can control what gets imported
    math_utils.py
    string_utils.py
"""

#* example content of __init__.py file 
    # from .math_utils import add
    # from .string_utils import to_upper
#* How to Import
# from my_package import add, to_upper
# print(add(2, 3))        # 5
# print(to_upper("hi"))   # HI    

#* Because we put inside __init__.py, we can directly import from my_package
#* no need to write like this from my_package.math_utils impoer add

#* Why __init__.py Matters ??
"""
1. Makes Python treat the folder as a package (so import works)
2. Can define package-level variables or constants and
3. define a perticualr function to run on importing a the package 
4. Can control what'ss visible with __all__"
"""

# importing my_package
import my_package
print(my_package.PACKAGE_VERSION)

from my_package import * 
# print(add(2,3))
# print(_internal_helper())  # will throw error if in __init__.py file has if _internal_helper is not insde __all__=[] 

# to use private function --> have to import like this 
from my_package import _internal_helper
print(_internal_helper()) 



#* Nested Packages
# A FastAPI project often looks like:
"""
app/
    __init__.py
    main.py
    routes/
        __init__.py
        users.py
        products.py
    models/
        __init__.py
        user.py
        product.py
"""
#* Inside routes/__init__.py:
"""
from .users import router as users_router
from .products import router as products_router
"""
#* Inside main.py:
"""
from fastapi import FastAPI
from app.routes import users_router, products_router

app = FastAPI()
app.include_router(users_router)
app.include_router(products_router)

"""