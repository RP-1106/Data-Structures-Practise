class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #OPT[i,j] = price at which stcok is sold at min price i and j is current price???
        minprice=float('inf')
        profit=-0
        result=0
        for i in range(len(prices)):
            if prices[i]<minprice:
                minprice=prices[i]
            profit = max(profit,prices[i]-minprice)
        return profit
