'''
LeetCode - problem 387 - First Unique Character in a String
'''

def firstUniqChar(self, s):        
        letters='abcdefghijklmnopqrstuvwxy'
        index=[s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1
