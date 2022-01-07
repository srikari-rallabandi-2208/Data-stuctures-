

class Node:
    
    def __init__(self,data,next):
        self.data = data
        self.next = next
    
    @property    
    def data(self):
        return self.data
    
    @property
    def data(self,data):
        self.data = data
        
    @property
    def next(self):
        return self.next
    
    @property
    def data(self,next):
        self.next = next
        

class Stack:
    
    length = 0
    head = None
    tail = None
    
    def __init__(self,data):
        node = Node(data)
    