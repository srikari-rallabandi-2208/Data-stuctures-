'''
LeetCode - problem 86
'''

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        def addNodesToLinkedList(currentNode, array):
            for num in array:
                node = ListNode(num)
                currentNode.next = node
                currentNode = currentNode.next
            return currentNode
        
        smaller,greater = [],[]
        while head:
            if head.val < x:
                smaller.append(head.val)
            else:
                greater.append(head.val)
            head = head.next
        start = ListNode(-1)
        currentNode = start
        currentNode = addNodesToLinkedList(currentNode, smaller)
        addNodesToLinkedList(currentNode, greater)
        return start.next
