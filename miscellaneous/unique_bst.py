'''
LeetCode - problem 96 - Dynamic Programming
'''

def numTrees(self, n):
        return factorial(2*n)//factorial(n)//factorial(n)//(n+1)
