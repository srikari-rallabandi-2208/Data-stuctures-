'''
LeetCode - problem 1376
'''

def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = collections.defaultdict(list)
        head = manager.index(-1)
        for emp,man in enumerate(manager):
            graph[man].append(emp)
        q = collections.deque()
        q.append((head,0))
        maxT=0
        while q:
            for i in range(len(q)):
                emp,t = q.popleft()
                maxT=max(maxT, t)
                for nei in graph[emp]:
                    neiT=informTime[emp]+t
                    q.append((nei,neiT))
        return maxT
