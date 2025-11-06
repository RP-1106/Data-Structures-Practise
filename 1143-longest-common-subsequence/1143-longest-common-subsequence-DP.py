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
                    #take max common length amongst when you compare text1 with one less char and text2 with one less char
                    OPT[i][j]=max(OPT[i-1][j], OPT[i][j-1])
                else:
                    #if the characters match, 1 + longest common character for both texts of length reduced by 1
                    OPT[i][j]=OPT[i-1][j-1]+1
        return OPT[t1][t2]


        