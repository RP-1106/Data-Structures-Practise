class Solution(object):
    def lengthOfLongestSubstring(self, s):
        '''
        l=0
        r=0

        hash=set()
        length=0

        while r<len(s) and l<len(s):
            if s[r] not in hash:
                hash.add(s[r])
                length=max(length,r-l+1)
                r+=1

            else: 
                hash.remove(s[l])
                l+=1
                length = max(length,r-l+1)
                
        return length
        '''

        d={}
        l=0
        r=0
        res=0

        while l<=r and r<len(s):
            if s[r] not in d or d[s[r]]==0:
                d[s[r]]=d.get(s[r],0)+1
                res = max(res,r-l+1)

            else:
                d[s[r]]=d.get(s[r],0)+1
                while d[s[r]]>1:
                    d[s[l]]=d.get(s[l],0)-1
                    l+=1
            r+=1
        return res