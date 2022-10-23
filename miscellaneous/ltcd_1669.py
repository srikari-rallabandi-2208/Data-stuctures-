'''
LeetCode - problem 1669
'''

    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr=list1
        for count in range(b):
            if count==a-1:      
                start=curr      
            curr=curr.next   
        start.next=list2     
        while list2.next:    
            list2=list2.next
        list2.next=curr.next  
        return list1

