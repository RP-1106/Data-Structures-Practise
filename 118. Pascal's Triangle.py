class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        n = numRows
        if n==1:
            return [[1]]

        #n=4
        #i=0,1,2,3
        #j=0,1,2,3
        OPT=[]
        for i in range(n):
            result=[]
            for j in range(i+1):
                if j==0 or j==i:
                    result.append(1)
                else:
                    result.append(OPT[i-1][j-1]+OPT[i-1][j])
            OPT.append(result)
        return OPT




                
        
