    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        
        last_out = -1
        last_min = -1
        last_max = -1
        
        count = 0
        
        for i,n in enumerate(nums):
            
            if minK <= n <= maxK: 
                if n == minK : last_min = i
                if n == maxK : last_max = i
                count += max(min(last_min, last_max) - last_out, 0)
            else:
                last_out = i
            
        return count
