'''
LeetCode - problem 85
'''

from collections import deque 
class Solution:
  def left(self,arr,n):
    result = [-1]*n
    stack = deque()
    stack.append(0)
    for i in range(1,n):
      currH = arr[i] 
      if stack and arr[stack[-1]]<currH:
        result[i] = stack[-1] 
      else:
        while stack and arr[stack[-1]]>=currH:
          stack.pop() 
        if stack:
          result[i] = stack[-1] 
      stack.append(i)
    return result
    
  def right(self,arr,n):
    stack = deque()
    stack.append(n-1)
    result=[n]*n 
    for i in range(n-2,-1,-1):
      currH = arr[i]
      if stack and arr[stack[-1]]<currH:
        result[i] = stack[-1] 
      else:
        while stack and arr[stack[-1]]>=currH:
          stack.pop() 
        
        if stack:
          result[i] = stack[-1]
      stack.append(i)
    return result 
    
  def getMaxArea(self,arr,n):
    left = self.left(arr,n)
    right = self.right(arr,n)
    maxArea = 0 
    for i in range(n):
      currArea = ((right[i]-left[i])-1)*(arr[i])
      maxArea = max(maxArea,currArea)
    return maxArea
  
  def maximalRectangle(self,matrix):
    n = len(matrix)
    m = len(matrix[0])
    maxArea = 0 
    height=[0]*m 
    for i in range(n):
    
      for j in range(m):
        if matrix[i][j] == "0":
          height[j] = 0 
        else:
          height[j]+= int(matrix[i][j])
      maxArea = max(maxArea, self.getMaxArea(height,m))
    return maxArea
