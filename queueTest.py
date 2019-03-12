from Queue import Queue

d = 1
d2 = 2
d3 = 3
d4 = 4
d5 = 5

q = Queue()
print(q.isEmpty())  #Print True

q.enqueue(d)
q.enqueue(d2)
q.enqueue(d3)
q.enqueue(d4)
q.enqueue(d5)

temp = q.peek() 
print(temp)    #Print 1

temp = q.dequeue()
print(temp)    #Print 1

print(q.isEmpty())  # Print false

temp = q.peek()     #Print 2
print(temp)

temp = q.dequeue()
print(temp)    #Print 2

temp = q.peek()     #Print 3
print(temp)

temp = q.dequeue()
print(temp)    #Print 3

temp = q.peek()     #Print 4
print(temp)

print(q.isEmpty())  # Print false

temp = q.dequeue()
print(temp)    #Print 4

temp = q.peek()     #Print 5
print(temp)

temp = q.dequeue()
print(temp)    #Print 5


print(q.isEmpty())  # Print true