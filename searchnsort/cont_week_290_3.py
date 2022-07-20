'''
LeetCode - problem 2250
'''

class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        h = [[] for _ in range(101)]
        for x, y in rectangles:
            h[y].append(x)

        for i in range(len(h)):
            h[i].sort()

        result = []

        for x, y in points:
            c = 0
            for yy in range(y, 101):
                if not h[yy] or h[yy][-1] < x:
                    continue
                if h[yy][0] >= x:
                    c += len(h[yy])
                    continue
                l, r = 0, len(h[yy])-1
                while l < r:
                    mid = (l + r) // 2
                    if h[yy][mid] >= x:
                        r = mid
                    else:
                        l = mid + 1
                c += len(h[yy]) - l

            result.append(c)

        return result
        
