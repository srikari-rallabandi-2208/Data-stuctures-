'''
LeetCode - prblem 959
'''
def dfs(i,j,big_grid):
    
    if(i >= len(big_grid) or i < 0 or j < 0 or j >= len(big_grid[i]) or big_grid[i][j] == False):
        return
    
    big_grid[i][j] = False
    dfs(i+1, j, big_grid)
    dfs(i-1, j, big_grid)
    dfs(i, j-1, big_grid)
    dfs(i, j+1, big_grid)
    
class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        n = len(grid) * 3
        big_grid = [[True for j in range(n)] for i in range(n)]
        
        for i, row in enumerate(grid):
            for j, char in enumerate(row):
                if char == '/':
                    big_grid[3 * i][(3 * j) + 2] = False
                    big_grid[(3 * i) + 1][(3 * j) + 1] = False
                    big_grid[(3 * i) + 2][3 * j] = False
                elif char == '\\':
                    big_grid[3 * i][3 * j] = False
                    big_grid[(3 * i) + 1][(3 * j) + 1] = False
                    big_grid[(3 * i) + 2][(3 * j) + 2] = False
                
        region_count = 0
        for i in range(len(big_grid)):
            for j in range(len(big_grid)):
                
                if big_grid[i][j]:
                    region_count += 1
                    dfs(i, j, big_grid)
                    
                    
        return region_count
