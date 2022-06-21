'''
leetcode problem 441 - arranging coins
'''

def arrangeCoins(n):
    return int((-1 + (1 + 8*n) * 0.5) // 2)
