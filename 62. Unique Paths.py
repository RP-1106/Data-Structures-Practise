class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        '''
        OPT = [[0 for i in range(n)] for j in range(m)]
        for i in range(n):
            OPT[m-1][i]=1
        for i in range(m):
            OPT[i][n-1]=1

        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                OPT[i][j]=OPT[i+1][j]+OPT[i][j+1]
        return OPT[0][0]
        '''

        #Doing this with just one double loop filling
        #instead of filling base case separately
        OPT = [[0 for i in range(n)] for j in range(m)]

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i==m-1 or j==n-1:
                    OPT[i][j]=1
                else:
                    OPT[i][j]=OPT[i+1][j]+OPT[i][j+1]
        return OPT[0][0]
                

        
