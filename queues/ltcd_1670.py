'''
LeetCode - problem 1670
'''

class Node:
    def __init__(self,val,nxt=None,prev=None):
        self.val=val
        self.next=nxt
        self.prev=prev

class FrontMiddleBackQueue:
    def __init__(self):
        self.head = Node(-1)
        self.back = Node(-1)
        self.head.next = self.back
        self.back.prev = self.head
    
    def pushFront(self, val: int) -> None:
        self.head.next=Node(val,self.head.next,self.head)
        self.head.next.next.prev=self.head.next

    def pushMiddle(self, val: int) -> None:
        if self.head.next.val==-1:
            self.pushFront(val)
            return None
        slow=fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        slow=slow.prev
        slow.next=Node(val,slow.next,slow)
        slow.next.next.prev=slow.next
        
    def pushBack(self, val: int) -> None:
        self.back.prev=Node(val,self.back,self.back.prev)
        self.back.prev.prev.next=self.back.prev
	
    def popFront(self) -> int:
        res=self.head.next.val
        if res==-1:
            return -1
        self.head.next=self.head.next.next
        self.head.next.prev=self.head
        return res
	
    def popMiddle(self) -> int:
        if self.head.next.val==-1:
            return -1
        slow=fast=self.head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        res=slow.val
        slow=slow.prev
        slow.next=slow.next.next
        slow.next.prev=slow
        return res
	
    def popBack(self) -> int:    
        res=self.back.prev.val
        if res==-1:
            return -1
        self.back.prev=self.back.prev.prev
        self.back.prev.next=self.back
        return res
