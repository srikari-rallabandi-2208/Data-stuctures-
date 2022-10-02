'''
LeetCode - problem 2420
'''

    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        ans = []
        non_increasing_dp = [1] * len(nums)
        non_decreasing_dp = [1] * len(nums)
        def check_non_increasing():
            for i in range(1, len(nums)):
                if nums[i] <= nums[i - 1]:
                    non_increasing_dp[i] = non_increasing_dp[i - 1] + 1
            
        def check_non_decreasing():
            for i in range(len(nums) - 2, 0, -1):
                if nums[i] <= nums[i + 1]:
                    non_decreasing_dp[i] = non_decreasing_dp[i + 1] + 1
          
        check_non_increasing()
        check_non_decreasing()
       
	   
        for i in range(k, len(nums) - k):
            if  non_increasing_dp[i - 1] >= k and  non_decreasing_dp[i + 1] >= k:
                ans.append(i)
        return ans 
