'''
LeetCode - problem 363
'''

import bisect
import sys


class Solution:
    def maxSumSubmatrix(self, matrix, k):

        if not matrix:
            return 0

        def max_sum_array_no_larger_than_k(l, k):
            prefix_sums = [0]
            prefix_sum, max_sum = 0, -sys.maxsize
            for item in l:
                prefix_sum += item
                
                left = bisect.bisect_left(prefix_sums, prefix_sum - k)
                if left < len(prefix_sums):
                    max_sum = max(max_sum, prefix_sum - prefix_sums[left])
                   
                bisect.insort(prefix_sums, prefix_sum)
            return max_sum

        row_len = len(matrix)
        col_len = len(matrix[0])
        max_sum = -sys.maxsize
        
        for from_col in range(col_len):
            col_values = [0 for _ in range(row_len)]
            for to_col in range(from_col, col_len):
                for row in range(row_len):
                    col_values[row] = col_values[row] + matrix[row][to_col]
                curr_sum = max_sum_array_no_larger_than_k(col_values, k)
                max_sum = max(curr_sum, max_sum)
        return max_sum
