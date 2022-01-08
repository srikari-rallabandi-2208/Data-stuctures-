

class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
class Stack:
    
    size = 0
    
    def __init__(self):
        self.top = None
    
    def push(self,data):
        node = Node(data)
        if self.top is None:
            self.top = node
        else:
            temp = self.top
            node.next = temp
            self.top = node
        self.size += 1
    
    def pop(self):
        if self.size > 0  and self.top is not None:
            temp = self.top
            self.top = self.top.next
            self.size -= 1
            return temp.data
        else:
            raise Exception("Popping from Empty Stack!!!")
    
    def isEmpty(self):
        return self.size == 0
    
    def peek(self):
        if not self.isEmpty():
            return self.top.data
        else:
            raise Exception("Empty Stack")
        
    def __str__(self):
        out = ""
        if self.size == 0 or self.top is None:
            out = "Empty Stack"
        else:
            temp = self.top
            while temp:
                out+= str(temp.data) + "=>"
                temp = temp.next
            out =  out[:-2]   
        return out
                
if __name__ == "__main__":
    stack = Stack()

    for i in range(11):
        stack.push(i)
    
    print(f"Stack : {stack}") 
    val = stack.peek()
    print(f"Peeking: {val}")      
        
    for _ in range(1,12):
        val = stack.pop()
        print(f"Removed: {val}")
    
    print(f"Stack : {stack}")  
    
    try:
        val = stack.peek()
        print(f"Peeking: {val}")
    except:
        print("Caught exception trying to peek")
     