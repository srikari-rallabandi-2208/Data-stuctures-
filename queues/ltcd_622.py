'''
LeetCode - problem 622	
'''

class MyCircularQueue:

    def __init__(self, k: int):
        self.k=k
        self.queue=[]

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue.append(value)
        return True
      
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.queue.pop(0)
        return True
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[0]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[-1]

    def isEmpty(self) -> bool:
        if not self.queue:
            return True
        return False

    def isFull(self) -> bool:
        if len(self.queue)==self.k:
            return True
        return False
