# Basic Dictionary
person = {"name": "Alice", "age": 25}
print(person["name"])  # Alice

# Add/update:
person["name"] = "Rohan"  # update
person["city"] = "Kolkata"  # add

# Looping:
for key, value in person.items():
    print(key, value)
    print(person[key])


# json.dumps({}) ||  JSON.stringify()    
import json
data = {
    "name": "Rohan",
    "age": 21
}
json_data = json.dumps(data)
print(json_data, type(json_data))
print(data, type(data))

# json.loads(`json string`) || JSON.parse()
data = '{"name": "Bob", "age": 30}'
obj = json.loads(data)
print(obj, type(obj))
print(data, type(data))