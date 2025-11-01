class Solution(object):
    def minFallingPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)    
        if n==1:
            return grid[0][0]

        OPT = [[float('inf') for i in range(n)] for j in range(n)]

        for i in range(n):
            for j in range(n):
                if i==0:
                    OPT[i][j]=grid[i][j]
                else:
                    for k in range(n):
                        if k==j:
                            continue
                        else:
                            OPT[i][j] = min(OPT[i][j], grid[i][j] + OPT[i-1][k])
            #print("i:",i,"=",OPT[i])
        return min(OPT[n-1])
                    
