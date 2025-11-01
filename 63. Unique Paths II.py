class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        '''
        m = len(obstacleGrid) #no.of rows
        n = len(obstacleGrid[0]) #no.of columns

        if obstacleGrid[m-1][n-1]==1 or obstacleGrid[0][0]==1:
            return 0

        OPT=[[-1 for j in range(n)] for i in range(m)]

        def last_column(OPT,i,n):
            for j in range(i-1,-1,-1):
                OPT[j][n-1]=0

        #make all the cells in the last row 1 but if you encounter a 1, all cells above it by 0
        for i in range(m-1,-1,-1):
            if obstacleGrid[i][n-1]==1:
                OPT[i][n-1]=0
                last_column(OPT,i,n)
                break
            else:
                OPT[i][n-1]=1

        def last_row(OPT,i,m):
            for j in range(i-1,-1,-1):
                OPT[m-1][j]=0

        for i in range(n-1,-1,-1):
            if obstacleGrid[m-1][i]==1:
                OPT[m-1][i]=0
                last_row(OPT,i,m)
                break
            else:
                OPT[m-1][i]=1
           
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                if obstacleGrid[i][j]==1:
                    OPT[i][j]=0
                else:
                    OPT[i][j]=OPT[i+1][j]+OPT[i][j+1]
        return OPT[0][0]
        '''

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[m-1][n-1]==1 or obstacleGrid[0][0]==1:
            return 0

        OPT=[[-1 for j in range(n)] for i in range(m)]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if obstacleGrid[i][j]==1:
                    OPT[i][j]=0
                elif i==m-1 and j==n-1:
                    OPT[i][j]=1
                elif i==m-1:
                    OPT[i][j]=OPT[i][j+1]
                elif j==n-1:
                    OPT[i][j]=OPT[i+1][j]
                else:
                    OPT[i][j]=OPT[i+1][j]+OPT[i][j+1]
        return OPT[0][0]
        
        
