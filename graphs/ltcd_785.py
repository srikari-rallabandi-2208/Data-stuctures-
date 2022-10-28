'''
LeetCode - problem 785
'''

    def isBipartite(self, graph: List[List[int]]) -> bool:
        glen = len(graph)
        s = []
        vis = [0] * glen
        for i in range(glen):
            if vis[i]: continue
            vis[i] = 1
            s.append(i)
            while len(s):
                curr = s.pop()
                edges = graph[curr]
                for next in edges:
                    if not vis[next]:
                        vis[next] = vis[curr] ^ 3
                        s.append(next)
                    elif vis[curr] == vis[next]:
                        return False
        return True
