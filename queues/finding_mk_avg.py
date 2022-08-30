'''
LeetCode - problem 1825
'''

from sortedcontainers import SortedList

class MKAverage:

    def __init__(self, m: int, k: int):
        self.arr = SortedList()
        self.m = m
        self.k = k
        self.q = deque()
        self.total = None

    def addElement(self, num: int) -> None:
        self.q.append(num)
        m = self.m
        k = self.k
        if len(self.q) > m:
            val = self.q.popleft()            
            ind1 = self.arr.bisect_left(val)
            ind2 = self.arr.bisect_right(val)
            left, right, mid = False, False, False
            kth, mth = self.arr[k], self.arr[m - k - 1]
            if k <= ind1 < m - k or k <= ind2 - 1 < m - k or (ind1 <= k and  m - k <= ind2 - 1 < m):
                mid = True
            elif ind1 < k:
                left = True
            elif ind2 - 1 >= m - k:
                right = True            
            
            self.arr.remove(val)
            ind1 = self.arr.bisect_left(num)
            ind2 = self.arr.bisect_right(num)            
            self.arr.add(num)            
            
            if k <= ind1 < m - k or k <= ind2 < m - k or (ind1 <= k and  m - k <= ind2 < m):
                if mid:
                    self.total += num - val
                if left:
                    self.total += num - kth
                if right:
                    self.total += num - mth
            elif ind1 < k:
                if mid:
                    self.total += self.arr[k] - val
                if left:
                    pass
                if right:
                    self.total += self.arr[k] - mth
            elif ind2 >= m - k:
                if mid:
                    self.total += self.arr[m - k - 1] - val
                if left:
                    self.total += self.arr[m - k - 1] - kth
                if right:
                    pass
        else:
            self.arr.add(num)
            if self.total is None and len(self.arr) == self.m:
                self.total = sum(self.arr[k:m-k])
            

    def calculateMKAverage(self) -> int:
        if len(self.arr) < self.m:
            return -1
        
        return int(self.total / (self.m - 2 * self.k))
