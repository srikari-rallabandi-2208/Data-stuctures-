'''
This is the representation of the queue data structure

The difference between Stack and Queue is that Queue has to maintain
2 pointers front and rear where as Queue can work only 1 pointer that's
top since you push and pull from the top itself where as in case of Queue
you push from back and pull from the front.

'''

class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None


class Queue:
    
    size = 0
    
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    
    def enqueue(self,data):
        ''' 
        check if the front is empty if empty queue is empty you put 
        front and back pointer to the same node
        '''
        if self.front is None:
            self.front = Node(data)
            self.rear = self.front
        else:
            ''' have the current rear in a temp
                temp's next would be None
                have rear pointer as current Node 
                point temp's next to the rear pointer
            '''
            temp = self.rear
            self.rear = Node(data)
            if temp is not None:
                temp.next = self.rear
            
        self.size += 1    
        
    def size(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
    def dequeue(self):
        val = None
        if self.isEmpty():
            raise Exception('queue is empty')
        else:
            val = self.front.data
            temp = self.front
            self.front = temp.next
        return val

    def __str__(self):
        out = ""
        if self.size == 0:
            out = "Empty Queue!!!"
        else:
            temp = self.front
            while temp:
                out += str(temp.data) + " => "
                temp = temp.next
        return out[:-3]

'''Driver code '''
if __name__ == "__main__":    
    queue = Queue()
    
    for i in range (11):
        queue.enqueue(i)
    
    print(f"Queue : {queue}")
    
    for _ in range (3):
        val = queue.dequeue()
        print(f"Queue : {val}")
    
    print(f"Queue : {queue}")