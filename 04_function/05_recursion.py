def factorial(number):
    if (number == 1 or number == 0 or number < 0):
        return 1
    return number * factorial(number-1)

# Calling the function
print(factorial(5))
