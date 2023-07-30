'''
LeetCode - problem 328
'''

class Solution:
    def oddEvenList(self, head):
        
        if head is None : return None
            
        odd = head
        dum = evn = head.next
        
        while evn and evn.next:
            odd.next = odd.next.next
            evn.next = evn.next.next
            odd = odd.next
            evn = evn.next
            
        odd.next = dum

        return head
