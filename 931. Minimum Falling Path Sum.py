class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n = len(matrix)
        if n==1:
            return matrix[0][0]

        OPT=[[-1 for j in range(n)] for i in range(n)]

        for i in range(n):
            for j in range(n):
                if i==0:
                    OPT[i][j]=matrix[i][j]
                else:
                    if j==0:
                        OPT[i][j]=matrix[i][j]+min(OPT[i-1][j], OPT[i-1][j+1])
                    elif j==n-1:
                        OPT[i][j]=matrix[i][j]+min(OPT[i-1][j], OPT[i-1][j-1])
                    else:
                        OPT[i][j]=matrix[i][j]+min(OPT[i-1][j-1], OPT[i-1][j], OPT[i-1][j+1])
        return min(OPT[n-1])
