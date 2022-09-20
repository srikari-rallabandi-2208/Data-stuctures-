'''
LeetCode problem 2398
'''

    def maximumRobots(self, times: List[int], costs: List[int], budget: int) -> int:
        cur = i = 0
        n = len(times)
        s = SortedList()
        for j in range(n):
            cur += costs[j]
            s.add(times[j])
            if s[-1] + (j - i + 1) * cur > budget:
                s.remove(times[i])
                cur -= costs[i]
                i += 1
        return n - i
