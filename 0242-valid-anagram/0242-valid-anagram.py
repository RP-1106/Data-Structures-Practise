class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        n = len(s)
        d1={}
        d2={}
        for i in range(n):
            d1[s[i]] = d1.get(s[i],0)+1
            d2[t[i]] = d2.get(t[i],0)+1
        if d1==d2:
            return True
        else:
            return False
        