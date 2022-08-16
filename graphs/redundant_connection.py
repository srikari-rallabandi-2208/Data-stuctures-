'''
LeetCode - problem 684
'''

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            rootx = find(x)
            rooty = find(y)
            if rootx == rooty:
                return [x,y]
            else:#connect
                parent[rooty] = rootx
                
        for x,y in edges:
            res = union(x,y)
            if res:
                return res
