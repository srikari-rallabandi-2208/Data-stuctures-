'''
LeetCode - problem 13
'''

    def romanToInt(self, s):
        ns = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        r=0
        ps=0
        for i in range(len(s)):
            r+=ns[s[i]]
            if i>0 and ns[s[i-1]]<ns[s[i]]:
                r-=2*ns[s[i-1]]
        return r
