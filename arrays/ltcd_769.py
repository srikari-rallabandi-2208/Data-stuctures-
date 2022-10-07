'''
LeetCode - problem 769
'''

    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        idxsum = 0
        valsum = 0
        ans = 0
        for i, n in enumerate(arr):
            
            idxsum += i
            valsum += n
            
            if idxsum == valsum:
                ans += 1
        return ans
