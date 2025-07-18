# write a decorator that measure the time a function takes to execute
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} is rans in {end-start} time")
        return result
    return wrapper

def dummy_function(n):
    time.sleep(n)
    return "this is dummy function result"
    
wrapper = timer(dummy_function)
print(wrapper(2))


#* above is how you will call a function inside a function without a decorator #
# * now see how we can do the same with decorator --> 

@timer
def dummy_function2(n):
    time.sleep(n)
    return "this is dummy funciton-2 result"

dummy_function2(2)
# so understood one thing that what above syntax is doing 
"""
You are NOT calling cache() every time you call dummy_function2.
You're calling it once at definition time, and it returns the wrapper
"""