class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        i=len(s)-1
        while i>=0:
            if s[i]==" ":
                i-=1
            else:
                break
        count+=1
        j=i-1
        while j>=0 and s[j]!=" ":
            count+=1
            j-=1
        return count

        