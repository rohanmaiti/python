# Python Class Methods - Complete Guide

## 1. Types of Methods in Python Classes

### Instance Methods
- **Need `self` as first parameter**
- Can access and modify instance variables and class variables
- Called on an instance of the class
```python
def instance_method(self):
    return self.instance_var
```

### Static Methods
- **NO `self` parameter**
- Use `@staticmethod` decorator
- Cannot access instance or class variables directly
- Behave like regular functions but belong to the class namespace
```python
@staticmethod
def static_method():
    return "No self needed"
```

### Class Methods
- **Use `cls` instead of `self`**
- Use `@classmethod` decorator
- Can access and modify class variables
- Receive the class itself as first parameter
```python
@classmethod
def class_method(cls):
    return cls.class_var
```

---

## 2. The `self` Parameter Rules

### ✅ When defining methods:
- **Instance methods** → Always include `self` as first parameter
- **Static methods** → No `self` needed
- **Class methods** → Use `cls` instead

### ✅ When calling methods internally:
- **NEVER manually pass `self`** - Python does it automatically
```python
def method1(self):
    return "data"

def method2(self):
    return self.method1()  # ✅ Correct - no self passed
    # return self.method1(self)  # ❌ Wrong!
```

### ✅ Python automatically passes `self`:
```python
# What you write:
obj.method()

# What Python does internally:
ClassName.method(obj)  # Passes the instance automatically
```

---

## 3. Accessing Variables and Methods

### Instance Variables (via `self`):
```python
class MyClass:
    def __init__(self):
        self.instance_var = "unique to each object"
    
    def access_instance(self):
        print(self.instance_var)  # ✅ Must use self
```

### Class Variables (two ways):
```python
class MyClass:
    class_var = "shared by all objects"
    
    def access_class_var(self):
        print(MyClass.class_var)  # ✅ Via class name
        print(self.class_var)     # ✅ Also works via self
```

---

## 4. Private Methods

### Private Instance Method:
- Use double underscore `__` prefix
- Name mangling: `__method` becomes `_ClassName__method`
- Can only be called from within the class
```python
class User:
    def __private_method(self):  # Private
        return "secret"
    
    def public_method(self):
        return self.__private_method()  # ✅ Accessible internally

u = User()
# u.__private_method()  # ❌ AttributeError
u.public_method()  # ✅ Works
```

### Private Static Method:
```python
class Helper:
    @staticmethod
    def __private_static():  # Private static
        return "hidden"
    
    @staticmethod
    def public_static():
        return Helper.__private_static()  # ✅ Call via class name
```

### Private Class Method:
```python
class Counter:
    __count = 0
    
    @classmethod
    def __private_class_method(cls):  # Private class method
        cls.__count += 1
    
    @classmethod
    def public_class_method(cls):
        cls.__private_class_method()  # ✅ Accessible internally
```

---

## 5. Summary Checklist

### ✅ DO:
- Include `self` in instance method definitions
- Use `@staticmethod` when you don't need instance/class data
- Use `@classmethod` when you need to access/modify class variables
- Use `self.method()` to call other instance methods
- Use `self.variable` to access instance variables
- Let Python automatically pass `self` when calling methods

### ❌ DON'T:
- Forget `self` in instance method definitions
- Manually pass `self` when calling methods: `self.method(self)` ❌
- Try to access `self` in static methods
- Use instance variables without `self.` prefix

---

## 6. Quick Reference

| Method Type | Decorator | First Parameter | Can Access Instance Data | Can Access Class Data |
|-------------|-----------|-----------------|-------------------------|----------------------|
| Instance    | None      | `self`          | ✅ Yes                  | ✅ Yes               |
| Static      | `@staticmethod` | None      | ❌ No                   | Only via class name  |
| Class       | `@classmethod` | `cls`       | ❌ No                   | ✅ Yes               |

---

## 7. Complete Example

```python
class Employee:
    company = "TechCorp"  # Class variable
    
    def __init__(self, name, salary):
        self.name = name           # Instance variable
        self.__salary = salary     # Private instance variable
    
    # Instance method
    def get_details(self):
        return f"{self.name} works at {self.company}"
    
    # Private instance method
    def __calculate_bonus(self):
        return self.__salary * 0.1
    
    # Public method using private method
    def show_bonus(self):
        return self.__calculate_bonus()
    
    # Static method
    @staticmethod
    def is_workday(day):
        return day not in ['Saturday', 'Sunday']
    
    # Class method
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company
    
    # Private static method
    @staticmethod
    def __private_helper():
        return "Internal calculation"
    
    # Private class method
    @classmethod
    def __private_class_helper(cls):
        return cls.company

# Usage:
emp = Employee("Rohan", 50000)
print(emp.get_details())           # Instance method
print(emp.show_bonus())            # Access private method
print(Employee.is_workday("Monday"))  # Static method
Employee.change_company("NewCorp")    # Class method
```
