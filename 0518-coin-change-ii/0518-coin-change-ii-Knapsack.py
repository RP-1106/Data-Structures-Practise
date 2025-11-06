class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """

        n = len(coins)
        #target = amount
        OPT=[[0 for j in range(amount+1)] for i in range(n+1)]
        # BASE CASE: 1 way to make amount 0 (use no coins)
        for i in range(n + 1):
            OPT[i][0] = 1
                 
        for i in range(1,n+1):
            for t in range(1,amount+1):
                if t<coins[i-1]:
                    OPT[i][t] = OPT[i-1][t]
                else:
                    OPT[i][t]=OPT[i-1][t]+OPT[i][t-coins[i-1]]
        return OPT[n][amount]

        
        