'''
LeetCode - problem 2178 - Greedy algo
'''

    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        arr = []
        if finalSum % 2 == 0:
            a, i = finalSum // 2, 1 
            while i <= a: 
                arr.append(2*i) 
                a -= i 
                i += 1 
            s = sum(arr)
            arr[-1] += finalSum - s
        return arr
