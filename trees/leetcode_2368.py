'''
LeetCode - problem 2368
'''

    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        res = set(restricted)
        graph = defaultdict(list)
        vis = set()
        
        for u, v in edges:
            if u in res or v in res: continue
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node):
            r = 1
            for nei in graph[node]:
                if nei in vis: continue
                vis.add(nei)
                r += dfs(nei)
            return r
        
        vis.add(0)
        return dfs(0)
