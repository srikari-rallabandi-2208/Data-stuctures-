'''
LeetCode - problem 2617
'''

class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        q = deque([[0, 0]])
        c = 0
        m, n = len(grid), len(grid[0])
        vis = set()
        row = [0 for _ in range(m)]
        col = [0 for _ in range(n)]
        while(q):
            l = len(q)
            c += 1
            for _ in range(l):
                i, j = q.popleft()
                if(i == m-1 and j == n-1):
                    return c
                val = grid[i][j]

                ii = max(col[j], i)+1
                while(ii < m and ii <= val+i):
                    if(ii == m-1 and j == n-1):
                        return c+1
                    if((ii, j) not in vis and grid[ii][j]):
                        q.append([ii, j])
                        vis.add((ii, j))
                        col[j] = ii
                    ii += 1
                
                jj = max(row[i], j)+1
                while(jj < n and jj <= val+j):
                    if(i == m-1 and jj == n-1):
                        return c+1
                    if((i, jj) not in vis and grid[i][jj]):
                        q.append([i, jj])
                        vis.add((i, jj))
                        row[i] = jj
                    jj += 1
        return -1
