class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        t1 = len(text1)
        t2 = len(text2)
        
        OPT=[[0 for j in range(t2+1)] for i in range(t1+1) ]

        for i in range(1,t1+1):
            for j in range(1,t2+1):
                if text1[i-1]!=text2[j-1]:
                    OPT[i][j]=max(OPT[i-1][j], OPT[i][j-1])
                else:
                    OPT[i][j]=OPT[i-1][j-1]+1
        return OPT[t1][t2]


        