class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        '''
        m = len(grid)
        n = len(grid[0])

        OPT=[[-1 for j in range(n)] for i in range(m)]

        #BASE CASE
        OPT[0][0]=grid[0][0]
        for i in range(1,n):
            OPT[0][i]= grid[0][i] +OPT[0][i-1]
        for i in range(1,m):
            OPT[i][0]= grid[i][0] +OPT[i-1][0]
        
        for i in range(1,m):
            for j in range(1,n):
                OPT[i][j]= min(grid[i][j]+ OPT[i-1][j],
                               grid[i][j]+ OPT[i][j-1])
        return OPT[m-1][n-1]
        '''

        m = len(grid)
        n = len(grid[0])

        OPT=[[-1 for j in range(n)] for i in range(m)]       
        
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    OPT[i][j] = grid[i][j]
                elif i==0:
                    OPT[i][j]=grid[i][j] + OPT[i][j-1]
                elif j==0:
                    OPT[i][j]= grid[i][j] +OPT[i-1][j]
                else:
                    OPT[i][j]= grid[i][j] + min(OPT[i-1][j], OPT[i][j-1])
        return OPT[m-1][n-1]






        
