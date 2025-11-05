class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount==0:
            return 0

        if len(coins)==1 and amount%coins[0]!=0:
            return -1

        n=amount+1
        OPT=[float('inf') for i in range(n)]
        OPT[0]=0

        for i in range(1,n):
            for j in coins:
                if j<=i:
                    OPT[i]=min(OPT[i],OPT[i-j]+1)
        if OPT[n-1]==float('inf'):
            return -1
        else:
            return OPT[n-1]