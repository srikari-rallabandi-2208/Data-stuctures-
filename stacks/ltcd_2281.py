'''
LeetCode - problem 2281
'''

def totalStrength(self, strength: List[int]) -> int:
        presums = [0] * (len(strength) + 2)
        curr_sum = 0
        
        for i in range(len(strength)):
            curr_sum += strength[i]
            presums[i + 1] = (presums[i] + curr_sum)
            
        strength.append(-1)
        stack = []
        total = 0
        MOD = 1e9 + 7
        
        for i in range(len(strength)):
            while stack and strength[stack[-1]] > strength[i]:
                idx = stack.pop()
                left = stack[-1] if stack else -1
                total += strength[idx] * ((idx - left) * (presums[i] - presums[idx]) - ((i - idx) * (presums[idx] - presums[left])))
            stack.append(i)
            
        return total % (10 ** 9 + 7)
