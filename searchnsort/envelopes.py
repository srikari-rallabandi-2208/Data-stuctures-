'''
LeetCode - problem 354
'''

class Solution(object):
    def maxEnvelopes(self, envs):
        def liss(envs):
            def lmip(envs, tails, k):
                b, e = 0, len(tails) - 1
                while b <= e:
                    m = (b + e) >> 1
                    if envs[tails[m]][1] >= k[1]:
                        e = m - 1
                    else:
                        b = m + 1
                return b
            
            tails = []
            for i, env in enumerate(envs):
                idx = lmip(envs, tails, env)
                if idx >= len(tails):
                    tails.append(i)
                else:
                    tails[idx] = i
            return len(tails)
        
        
        def f(x, y):
            return -1 if (x[0] < y[0] or x[0] == y[0] and x[1] > y[1]) else 1
            
        envs.sort(cmp=f)
        return liss(envs)
