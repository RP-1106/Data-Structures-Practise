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
            options = []
            if len(coins)==1 and amount%coins[0]!=0:
                OPT[i]=-1
                continue
            for j in coins:
                if j<=i:
                    options.append(OPT[i-j]+1)
            if len(options)==0:
                OPT[i]=-1
            else:
                OPT[i]=min(options)
        return OPT[n-1]