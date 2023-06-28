'''
LeetCode - problem 2528
'''

    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        lo, hi = min(stations), sum(stations) + k
        ans = lo
        while lo <= hi:
            mid = (lo + hi) // 2
            ts, left = stations[:], k
            cur = sum(ts[:r + 1])
            if cur < mid:
                left -= mid - cur
                ts[r] += mid - cur
                cur = mid
            for i in range(1, len(ts)):
                if i + r < len(ts): cur += ts[i + r]
                if i - r - 1 >= 0: cur -= ts[i - r - 1]
                if cur < mid:
                    left -= mid - cur
                    ts[min(i + r, len(ts) - 1)] += mid - cur
                    cur = mid
                if left < 0: break
            if left >= 0:
                ans = max(ans, mid)
                lo = mid + 1
            else: hi = mid - 1
        return ans
