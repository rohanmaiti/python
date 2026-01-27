# Normal function - returns all at once
def normal_func():
    return [1, 2, 3]

result = normal_func()
# print(result)  # [1, 2, 3] - entire list in memory

# Generator function - returns one at a time
def generator_func():
    yield 1
    print("abc")
    print("xyz")
    yield 2
    print("ljdhflahd")
    yield 3

gen = generator_func()
# First next() - runs until first yield
print(next(gen))  
# Output: 1

# Second next() - resumes and runs until second yield
print(next(gen))  
# Output: abc
#         xyz
#         2   # as 2 is being returned 

# Third next() - resumes and runs until third yield
print(next(gen))  
# Output: ljdhflahd
#         3   # as 3 is being returned 

# Fourth next() - no more yields, raises StopIteration
print(next(gen))  
# Output: StopIteration error