'''
LeetCode - problem 685
'''

    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        from collections import Counter, deque, defaultdict
        ic = Counter()  # incoming edges
        oc = Counter()  # outcoming edges
        total = []
        for x in edges:
            total += x
        total = set(total)  # set(all nodes)
        for e in edges:
            ic[e[1]] += 1
            oc[e[0]] += 1
		# All nodes in tree should have one incoming edge except root with zero
        for k, v in ic.items():
            if v == 2:
			    # case 1: one incoming edge in these two is redundant
                possibles = list(filter(lambda x: x[1] == k, edges))
                if self.dfs(edges, total, possibles[1]):
                    return possibles[1]
                else:
                    return possibles[0]
        # case 2: root gets an incoming edge, form a cycle            
        return self.unionfind(edges, total)
        
        
    def dfs(self, edges, total, re_edge):
        visited = set()
        stack = deque()
        ic = Counter()
        oc = defaultdict(list)
        for e in edges:
            if e != re_edge:
                ic[e[1]] += 1
                oc[e[0]].append(e[1])
        root = None
        for n in total:
            if ic[n] == 0:
                root = n
                break
        stack.append(root)
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                for x in oc[node]:
                    stack.append(x)
        return len(visited) == len(total)
            
        
    def unionfind(self, edges, total):
        union = defaultdict(int)
        for n in total:
            union[n] = n
        for i in range(len(edges)):
            if union[edges[i][0]] == union[edges[i][1]]:
                return edges[i]
            else:
                u = union[edges[i][1]]
                for k, _ in union.items():
                    if union[k] == u:
                        union[k] = union[edges[i][0]]
