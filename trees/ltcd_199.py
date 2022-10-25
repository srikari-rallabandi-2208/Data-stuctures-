'''
LeetCode - problem 199
'''

def rightSideView(self, root):
    ans = []
    self.h = -1
    def prog(root,height):
        if root is None:
            return
        if height > self.h:
            ans.append(root.val)
            self.h = height
        prog(root.right, height + 1)
        prog(root.left, height + 1)
    prog(root,0)
    return ans
