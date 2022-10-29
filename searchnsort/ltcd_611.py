'''
LeetCode - problem 611
'''

    def triangleNumber(self, nums: List[int]) -> int:
        nums=sorted(nums)
        c=0
        for i in range(len(nums)-1,-1,-1):
            j,k=0,i-1
            while j<k:
                if nums[j]+nums[k]>nums[i]:
                    c+=k-j
                    k-=1
                else:
                     j+=1
        return c

