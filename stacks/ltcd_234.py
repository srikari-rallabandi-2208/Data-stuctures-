'''
LeetCode - problem 234
'''

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        middle = slow
        prev, actual = None, middle
        while actual:
            nxt = actual.next
            actual.next = prev
            prev = actual
            actual = nxt
        l, r = head, prev
        while r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
        return True
