'''
LeetCode - problem 122
'''

    def maxProfit(self, prices):
        return sum([ prices[i]-prices[i-1] for i in range(1,len(prices)) if prices[i]>prices[i-1] ])
