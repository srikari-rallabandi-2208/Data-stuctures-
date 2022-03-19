'''
leetcode problem 1051 - height checker
'''

def heightChecker(self, heights: List[int]) -> int:
    sorted_list=sorted(heights)
    output=0
    for i in range(len(heights)):
        if heights[i]!=sorted_list[i]:
            output+=1
            
    return output
