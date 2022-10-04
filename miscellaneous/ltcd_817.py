'''
LeetCode - problem 817
'''

    def numComponents(self, head: ListNode, G: List[int]) -> int:
        count = 0
        i = head
        while i:
            if i.val in G:
                count += 1
                while i and i.val in G:
                    i = i.next
            else :
		i = i.next
        return count
