'''
LeetCode - problem 100
'''

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return 1
        if not p or not q:
            return 0
        return p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
