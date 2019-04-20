from Queue import Queue

d = 1
d2 = 2
d3 = 3
d4 = 4
d5 = 5

q = Queue()
print(q.isEmpty())  #Print True

print("Inserting Values into Queue")
q.enqueue(d)
q.enqueue(d2)
q.enqueue(d3)
q.enqueue(d4)
q.enqueue(d5)

print("Checking if queue is not Empty:")
if not q.isEmpty():  # Print false
    print("Test successful!")
else:
    print("Test unsuccessful")

print("Dequeue Test:")    
q.dequeue()
if q.peek() == 2:
    print("Test successful!")
else:
    print("Test unsuccessful")

print("Dequeue Test:")     
q.dequeue()
if q.peek() == 3:
    print("Test successful!")
else:
    print("Test unsuccessful")

print("Dequeue Test:") 
q.dequeue()
if q.peek() == 4:
    print("Test successful!")
else:
    print("Test unsuccessful")
    
print("Dequeue Test:") 
q.dequeue()
if q.peek() == 5:
    print("Test successful!")
else:
    print("Test unsuccessful")
q.dequeue()

print("Checking if queue is Empty:")
if q.isEmpty():
    print("Test successful!")
else:
    print("Test unsuccessful")