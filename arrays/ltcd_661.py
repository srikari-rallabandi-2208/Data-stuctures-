'''
LeetCode - problem 661
'''

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        res = [[0]*n for i in range(m)]
        
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        for i in range(m):
            for j in range(n):
                cur_sum = img[i][j]
                count = 1
                for d in dirs:
                    x = i + d[0]
                    y = j + d[1]
                    if 0 <= x < m and 0 <= y < n:
                        count += 1
                        cur_sum += img[x][y]
                res[i][j] = int(cur_sum / count)
        
        return res
