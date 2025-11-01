class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0 or n==1:
            return 1

        OPT=[-1]*(n+1)
        OPT[0]=1
        OPT[1]=1

        for i in range(2,n+1):
            OPT[i]=OPT[i-1]+OPT[i-2]
        return OPT[n]
