class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepest_leaves_sum(self, root):
        def dfs1(root):
            if not root: return 0
            return max(dfs1(root.left), dfs1(root.right))+1
        def dfs2(root, dep):
            if not root: return
            if dep == max_depth: self.total += root.val
            dfs2(root.left, dep+1)
            dfs2(root.right, dep+1)
        self.total = 0
        max_depth = dfs1(root)
        dfs2(root, 1)
        return self.total

