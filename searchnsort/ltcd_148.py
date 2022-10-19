'''
LeetCode - problem 148
'''

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        nums = []
        currnode = head
        while currnode:
            nums.append(currnode.val)
            currnode = currnode.next
            
        nums.sort()
        currnode = head
        for i in nums:
            currnode.val = i
            currnode = currnode.next
            
        return head
