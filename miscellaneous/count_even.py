'''
LeetCode - problem 2180
'''

def countEven(self, num: int) -> int:
    return (num - sum(map(int, str(num))) % 2) // 2
