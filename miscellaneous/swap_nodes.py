'''
leetcode problem 24 - swap nodes in pairs
'''
class ListNode:
	def __init__(self, val = 0, next = None):
		self.val = val
		self.next = next


class Solution:
	def swapPairs(self, head):
		if head is None or head.next is None:
			return head
		else:
			temp = head
			head = head.next
			temp.next = head.next
			head.next = temp

			temp.next = self.swapPairs(temp.next)
	
		return head
