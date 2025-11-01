class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        n = rowIndex
        if n==0:
            return [1]

        OPT=[]
        for i in range(n+1):
            result=[]
            for j in range(i+1):
                if j==0 or j==i:
                    result.append(1)
                else:
                    result.append(OPT[i-1][j-1]+OPT[i-1][j])
            OPT.append(result)
        return OPT[n]
        
