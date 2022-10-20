'''
LeetCode - problem 786
'''

    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        left, right = 0, 1
        p, q = 0, 1
        n = len(arr)
        while True:
            cnt = 0
            p = 0
            m = (left+right)/2
            for i in range(n):
                j = n - 1 - i
                while j >= 0 and arr[i] > m*arr[n-1-j]:
                    j -= 1
                cnt += j+1
                if j >= 0 and q*arr[i] > p*arr[n-1-j]:
                    p = arr[i]
                    q = arr[n-1-j]
            if cnt < k:
                left = m
            elif cnt > k:
                right = m
            else:
                return [p, q]
