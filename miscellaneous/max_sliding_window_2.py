'''
leetcode problem number - 1687

delivering boxes from storage to ports


'''


def boxDelivering(self, boxes, portsCount, maxBoxes, maxWeight):
     
    n = len(boxes)
    que = collections.deque([(-1,0)])
    pre = -1
    ws = 0  
    for i, (p, w) in enumerate(boxes):  
        ws += w
        while i - pre > maxBoxes or ws > maxWeight:
            pre += 1
            ws -= boxes[pre][1]
        while que[0][0] < pre: que.popleft()
        mn = (2 if i+1<n and p==boxes[i+1][0] else 1) + que[0][1]
        while que[-1][1] >= mn: que.pop()  
        que.append((i, mn))
    base_trip = 1  
    for i in range(n-1):
        if boxes[i][0] != boxes[i+1][0]: base_trip += 1
        
    return base_trip + que[-1][1]

