'''
LeetCode - problem 33
'''

    def search(self, nums: List[int], target: int) -> int:
        def searchIndexOfMinElement(nums):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if (mid == left or nums[mid-1] > nums[mid]) and (mid == right or nums[mid] < nums[mid+1]):
                    return mid
                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        
        def binarySearch(nums, left, right, target):
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        
        pivot = searchIndexOfMinElement(nums)
        res = binarySearch(nums, 0, pivot - 1, target)
        if res != -1: return res
        return binarySearch(nums, pivot, len(nums) - 1, target)
