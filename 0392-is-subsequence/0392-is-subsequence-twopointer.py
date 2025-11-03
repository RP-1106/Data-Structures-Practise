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

        l1=0
        l2=0
        count=0
        while l1<=l2 and l1<len(s) and l2<len(t):
            if s[l1]==t[l2] and l1==len(s)-1:
                count+=1
                if count==len(s):
                    return True
                else:
                    return False
            elif s[l1]==t[l2] and l1<len(s):
                count+=1
                l1+=1
                l2+=1
            else:
                l2+=1
        if count==len(s):
            return True
        else:
            return False



        