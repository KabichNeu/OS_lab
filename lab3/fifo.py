# Python program to demonstrate
# working of FIFO
# using Queue interface in Java

q = []

# Adds elements {0, 1, 2, 3, 4} to queue
for i in range(5):
	q.append(i)

# Display contents of the queue.
print("Elements of queue-" , q)

# To remove the head of queue.
# In this the oldest element '0' will be removed
removedele = q.pop(0)
print("removed element-" , removedele)

print(q)

# To view the head of queue
head = q[0]
print("head of queue-" , head)

# Rest all methods of collection interface,
# Like size and contains can be used with this
# implementation.
size = len(q)
print("Size of queue-" , size)

