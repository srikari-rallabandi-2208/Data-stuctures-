'''
LeetCode - problem 2421
'''

class DSU:
    def __init__(self, n):
        self.roots = list(range(n))
    
    def join(self, left, right):
        self.roots[self.find(right)] = self.find(left)
    
    def find(self, value):
        if self.roots[value] != value:
            self.roots[value] = self.find(self.roots[value])
        return self.roots[value]


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        result = 0
        dsu = DSU(n)

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        vals_to_vertexes = defaultdict(lambda: [])
        for i, val in enumerate(vals):
            vals_to_vertexes[val].append(i)

        for value, vertexes in sorted(vals_to_vertexes.items()):
            for vertex in vertexes:
                for neighbour in graph[vertex]:
                    if vals[neighbour] <= value:
                        dsu.join(vertex, neighbour)
            
            roots = Counter()
            for vertex in vertexes:
                root_id = dsu.find(vertex)
                roots[root_id] += 1
                result += roots[root_id]
        
        return result
