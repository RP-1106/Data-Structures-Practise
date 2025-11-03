class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s=="" and t=="":
            return True
        if len(s)>0 and t=="":
            return False
        if len(t)>0 and s=="":
            return True

        m=len(s)
        n=len(t)
        OPT=[[False for j in range(n+1)] for i in range(m+1)]
        for i in range(n+1):
            OPT[0][i]=True

        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1]==t[j-1]:
                    OPT[i][j]=OPT[i-1][j-1]
                else:
                    OPT[i][j]=OPT[i][j-1]
        return OPT[m][n]
        


