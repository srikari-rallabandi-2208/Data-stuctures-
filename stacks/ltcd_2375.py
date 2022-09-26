'''
LeetCode - problem 2375
'''

    def smallestNumber(self, pattern: str) -> str:
        stack = []
        res = ''
 
        for i in range(len(pattern) + 1):
            stack.append(i + 1)
            
            if (i == len(pattern) or pattern[i] == 'I'):
                while len(stack) > 0:
                    res += str(stack.pop())
        return res
