'''
leetcode problem 55 - jump game
'''

def can_jump(nums):
    target = len(nums)-1
    for i in range(target-1,-1,-1):
        if nums[i] + i >= target:
            target = i
    return target == 0
