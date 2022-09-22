'''
LeetCode - problem 753
'''

def crackSafe(self, n, k):
        def dfs(curr, counted, total):
            if len(counted)==total:
                return curr
            
            for i in range(k):
                tmp = curr[-(n-1):]+str(i) if n!=1 else str(i)
                if tmp not in counted:
                    counted.add(tmp)
                    res = dfs(curr+str(i), counted, total)
                    if res:
                        return res
                    counted.remove(tmp)
                    
        return dfs("0"*n, set(["0"*n]), k**n) 
