'''
LeetCode - poblem 1559
'''

def getAdjNodes(grid, r, c):
    return [(i, j) for i, j in [(r-1, c),  (r+1,c), (r,c-1), (r,c+1)]
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) ]

def isCycle(grid, r, c, prev, letter):
    grid[r][c] = ord(letter) # set to seen
    
    for i, j in getAdjNodes(grid, r, c):
        if prev != (i, j):
            adjNodeVal = grid[i][j]
            if adjNodeVal == letter:
                if isCycle(grid, i, j, (r, c), letter):
                    return True 
            elif adjNodeVal == ord(letter):
                return True

    return False


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if type(grid[r][c]) is str:
                    if isCycle(grid, r, c, ('tmp', 'tmp'), grid[r][c]):
                        return True 
        return False
