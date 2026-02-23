stack = []

stack.append(10)  # push
stack.append(20)
stack.append(30)
print("printing stack = ", stack)


top_element = stack.pop()       # pop
print("printing poped element = ", top_element)
print("printing stack = ", stack)


print("top element = ", stack[-1]) # peek