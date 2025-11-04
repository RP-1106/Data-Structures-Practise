class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 1

        OPT=[0 for i in range(n+1)]
        OPT[1]=1
        OPT[2]=1

        for i in range(3,n+1):
            OPT[i]=OPT[i-3]+OPT[i-2]+OPT[i-1]
        return OPT[n]


        