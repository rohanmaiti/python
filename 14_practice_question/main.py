"""
Q1).
Create a variable user that stores a dictionary with name "Alice", age 25, and hobbies as a list containing "reading" and "coding".
Then print "Name: Alice, Age: 25" using f-string.
"""

data = {
    "name": "Alice",
    "age": 25,
    "hobbies": ["reading", "coding"]
}
print(f"Name = {data["name"]}, age = {data.get('age')} hobbies = {(", ").join(data['hobbies'])}")



"""
Q2).
Write a function greet_user(name, age=18) that:
Returns "Hello Alice, you are 25 years old." if name="Alice" and age=25
Uses default age 18 if not provided.
"""
def greet_user(name, age=18):
    return f"Hello {name}, you are {age} years old"

print(greet_user("Rohan", 21))


"""
Q3). 
Create a class Car with:
An __init__ method taking brand and year
A method get_info() returning "<brand> - <year>"
Create an object for "Tesla", 2024 and call get_info().
"""

class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    def get_info(self):
        return f"<{self.brand}> - <{self.year}>"

tesla = Car("Tesla", 2024)
print(tesla.get_info()); 



"""
Q4). # Given:
import json
data = '{"name": "John", "age": 30}'
Convert data into a Python dictionary, change the "age" to 35, and then convert it back to JSON.
"""






"""
Q5). Exception Handling
Write code that takes a number input and prints its square, but if the user enters something 
that's not a number, print "Invalid input".
"""




"""
Q6). Async Basics
Write an async function say_hello() that waits 2 seconds and then prints "Hello from async".
Then run it.
"""
