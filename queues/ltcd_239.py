'''
LeetCode - problem 239
'''

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k > len(nums) or not nums:
            return []
        
        ret = []
        q = deque()
        
        for i in range(len(nums)):
            while q and q[-1][0] <= nums[i]:
                q.pop()
            q.append((nums[i], i))
            while q[0][1] <= i - k:
                q.popleft()
            if i >= k - 1:
                ret.append(q[0][0])
        
        return ret
