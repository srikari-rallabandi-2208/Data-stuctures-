'''
LeetCode - problem 1782
'''

def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
    degrees = [0]*(n+1)
    edgeCount = defaultdict(int)
    
    for u,v in edges:
        degrees[u]+=1
        degrees[v]+=1
        if u>v:
            u,v = v,u
        edgeCount[(u,v)]+=1
        
    sortedDegrees = sorted(degrees)[1:]
    res = []
    
    for val in queries:
        count = 0
        r = n
        for l in range(n-1):
            while r-1>l and sortedDegrees[l]+sortedDegrees[r-1]>val:
                r-=1
            if r>l:
                count+=n-r
            else:
                count+=n-l-1

        for u,v in edgeCount:
            if degrees[u]+degrees[v]>val and degrees[u]+degrees[v]-edgeCount[(u,v)]<=val:
                count-=1
        
        res.append(count)
        
    return res
