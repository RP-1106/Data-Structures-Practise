class Solution(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1:
            return False
        #INDEX0=>N=1
        #index1=>n=2
        OPT=[False for i in range(n+1)]
        for i in range(2,n+1):
            OPT[i]=False
            for x in range(1,i):
                if i%x==0:
                    if OPT[i-x]==False:
                        OPT[i]=True
                        break
        return OPT[n]

        
        