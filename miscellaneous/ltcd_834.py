'''
LeetCode - problem 834
'''

class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        if N == 1: return [0]
        
        neighbors = collections.defaultdict(set)
        for n1,n2 in edges:
            neighbors[n1].add(n2)
            neighbors[n2].add(n1)
        dis2child = [0] * N
        population = [1] * N
        dis2all = [0] * N
         
        def dfs1(node = 0,parent = None):
            for child in neighbors[node]:
                if child != parent:
                    dfs1(child,node)
                    population[node] += population[child]
                    dis2child[node] += dis2child[child] + population[child]
            return
        dis2all = dis2child
        def dfs2(node = 0,parent = None):
            for child in neighbors[node]:
                if child != parent:
                    dis2all[child] = dis2all[node] + N - 2*population[child]
                    dfs2(child,node)
                    
        dfs1()
        dfs2()
        return dis2all
