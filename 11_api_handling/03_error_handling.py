# syntax

#************** Example 01 **********
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid number")


#************** Example 02 ***********
try:
    f = open("data.txt", "r")
except FileNotFoundError:
    print("File not found")
else:
    print(f.read())
finally:
    print("Closing resources...")
