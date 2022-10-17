'''
LeetCode - problem 2073
'''

from collections import deque


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque()

        for person, ticket in enumerate(tickets):
            if person == k:
                queue.append((True, ticket))
            else:
                queue.append((False, ticket))

        passes = 0
        processed = 0

        while True:
            flag, ticket = queue.popleft()

            if flag:
                passes += processed + 1
                processed = 0
                ticket -= 1

                if ticket:
                    queue.append((True, ticket))
                    continue

                break

            ticket -= 1
            processed += 1

            if ticket:
                queue.append((False, ticket))

        return passes
