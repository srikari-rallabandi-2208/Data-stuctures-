'''
LeetCode - problem 2415
'''
    from collections import defaultdict

    def reverseOddLevels(self, root):
        odd_level_nodes = defaultdict(list)

        def reverse(root, level=0, side=None):
            if root is None:
                return None

            if level % 2 == 1:
                if side == "right":
                    odd_level_nodes[level].append(root)
                else: 
                    mirror_root = odd_level_nodes[level].pop()
                    root.val, mirror_root.val = mirror_root.val, root.val

            root.right = reverse(root.right, level+1, "right" if side is None else side)
            root.left = reverse(root.left, level+1, "left" if side is None else side)
            return root

        return reverse(root)
