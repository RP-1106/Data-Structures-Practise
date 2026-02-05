class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if s==t:
            return 0
        if len(s)==1 and s[0] in t:
            return 1
        if len(s)==1 and s[0] not in t:
            return len(t)

        i,j=0,0
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                j+=1
            i+=1
        if j==len(t):
            return 0
        else:
            return len(t)-j