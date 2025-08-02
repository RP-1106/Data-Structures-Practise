class Solution(object):
    def maxProfit(self, prices):
        maxp=0
        minp=float('Inf')
        profit=0

        for i in prices:
            if i<minp:
                minp=i
                maxp=0
            
            elif i>maxp:
                maxp=i
                profit=max(maxp-minp,profit)
        return profit
