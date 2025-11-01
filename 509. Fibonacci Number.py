class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        #METHOD 1:
        #TIME COMPLEXITY: O(N)
        #SPACE COMPLEXITY: O(N)
        #SPECIFY BASE CASES
        if n==0:
            return 0
        elif n==1:
            return 1

        #opt array
        OPT=[-1]*(n+1)
        OPT[0]=0
        OPT[1]=1

        for i in range(2,n+1):
            OPT[i]=OPT[i-1]+OPT[i-2]
        return OPT[n]
        '''

        #METHOD 2:
        #TIME COMPLEXITY: O(N)
        #SPACE COMPLEXITY: O(1)
        prev2=0
        prev=1

        #BASE CASE
        if n==0:
            return 0
        elif n==1:
            return 1

        for i in range(2,n+1):
            cur = prev2+prev
            prev2=prev
            prev=cur
        return prev
