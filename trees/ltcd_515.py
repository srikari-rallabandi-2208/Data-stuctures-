'''
LeetCode - problem 515
'''

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(st):
            m = -inf
            new = []
            while(st):
                x = st.pop()
                m = max(m, x.val)
                if x.left:
                    new.append(x.left)
                if x.right:
                    new.append(x.right) 
            ans.append(m)
            if new:
                dfs(new)
            else:
                return
            
        if not root:
            return []
        dfs([root])
        return ans
