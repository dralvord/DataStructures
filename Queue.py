class Node:
    data = None
    prev = None
    next = None
    
    def __init__(self, data):
        self.data = data
        
class Queue:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, newData):
        newNode = Node(newData)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
            
    def dequeue(self):
        if self.head != None:
            if self.head.next == None:
                temp = self.head
                self.head = None
                return temp.data
            else:
                temp = self.head
                self.head = self.head.next
                return temp.data
        
        
    def peek(self):
        if self.head != None:
            return self.head.data
        
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
