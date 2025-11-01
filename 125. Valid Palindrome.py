class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=0
        r=len(s)-1
        s = s.lower()

        while r>=l:
            while l<=r and s[l].isalnum()==0 :
                l+=1
            while l<=r and s[r].isalnum()==0 :
                r-=1
            if l<=r and s[l]!=s[r]:
                return False
            else:
                l+=1
                r-=1     
        return True
        
