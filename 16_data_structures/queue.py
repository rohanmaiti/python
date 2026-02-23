from collections import deque

q = deque()

q.append(10) # enqueue
q.append(20)
q.append(30)

print("printing queue = ", q)
print(q[0]) # peek

item = q.popleft() # dequeue
print("dequeue item = ", item)
print("printing queue after dequeue = ", q)


