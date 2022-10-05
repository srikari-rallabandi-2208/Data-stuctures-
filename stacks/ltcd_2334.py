'''
LeetCode - problem 2334
'''

    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        nums.append(0)
        stack = [-1]
        for i in range(len(nums)):
            while nums[stack[-1]]>nums[i]:
                w = i-stack[-2]-1
                if nums[stack.pop()] > threshold / w:
                    return w
            stack.append(i)
        return -1
