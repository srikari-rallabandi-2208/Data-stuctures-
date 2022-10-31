'''
LeetCode - problem 49
'''

    def groupAnagrams(self, strs):
        m = collections.defaultdict(list)
        for s in strs:
            m["".join(sorted(s))].append(s)
        return [v for v in m.values()]
