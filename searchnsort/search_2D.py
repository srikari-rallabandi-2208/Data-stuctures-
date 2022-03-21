'''
leetcode problem 74 - search a 2D matrix
'''

def binary_search(nums, target):
    l, e = 0, len(nums)-1

    while l <= e:
        m = (l+e)//2
        if nums[m] == target : return True
        elif nums[m] > target : e = m-1
        else : l = m+1

    return False

def searchMatrix(self, matrix, target):
    fr, lr, lc = 0, len(matrix)-1, len(matrix[0])-1

    while fr <= lr:
        mr = (fr+lr)//2
        if(matrix[mr][0] <= target and matrix[mr][lc] >= target):
            return binary_search(matrix[mr], target)
        elif(matrix[mr][lc] < target): fr = mr+1
        else: lr = mr-1

    return False
