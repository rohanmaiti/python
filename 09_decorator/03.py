
# * implement a deocrator that caches the return values of a function, so that when it calles with the same
# * arguemts then it returns the result imidiately without calling the function again 
import time

def cache_value(func):
    dictionary = {} #* question why not it is initialising every time ???
    def wrapper(*args):
        normal_args = ', '.join([str(string) for string in args])
        if normal_args in dictionary:
            return f"caching result, {dictionary[normal_args]}"
        else:
            dictionary[normal_args] = func(*args)
            return dictionary[normal_args]
    return wrapper


@cache_value
def sum(a, b):
    time.sleep(4)
    return a+b

result = sum(1,2)
print(result)

result = sum(2,3)
print(result)

result = sum(1,2)
print(result)