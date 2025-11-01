class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        m=len(triangle)

        OPT=[[-1 for j in range(i+1)] for i in range(m)]
        OPT[0][0]=triangle[0][0]

        for i in range(1,m):
            for j in range(i+1):
                if j==0:
                    #Leftmost element can only come from above
                    OPT[i][j]= triangle[i][j] + OPT[i-1][j]
                elif j==i:
                    #Rightmost element can only come from diagonal
                    OPT[i][j]= triangle[i][j] + OPT[i-1][j-1]
                else:
                    #middle elements are minimum of above and diagonal to them
                    OPT[i][j]=triangle[i][j]+min(OPT[i-1][j-1], OPT[i-1][j])
        return min(OPT[m-1])

        
