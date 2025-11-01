class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l=0
        r=0

        hash=set()
        length=0

        while r<len(s) and l<len(s):
            if s[r] not in hash:
                hash.add(s[r])
                length=max(length,r-l+1)
                r+=1

            elif s[r] in hash:
                while s[l]!=s[r] and l<r:
                    hash.remove(s[l])
                    l+=1

                if s[l]==s[r]:
                    hash.remove(s[l])
                    l+=1

                length = max(length,r-l+1)
        return length
