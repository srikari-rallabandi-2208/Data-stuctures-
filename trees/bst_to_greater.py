def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        tot=0
        def dfs(node):
            nonlocal tot
            if not node:
                return 
            if node.right:
                dfs(node.right)
            tot=node.val=tot+node.val
            if node.left:
                dfs(node.left)
            return
        dfs(root)
        return root
