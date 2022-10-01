'''
LeetCode - problem 2331
'''

    def evaluateTree(self, root):
        if root.val <= 1: return root.val
        left, right = self.evaluateTree(root.left), self.evaluateTree(root.right)
        return (left or right) if root.val == 2 else (left and right)
