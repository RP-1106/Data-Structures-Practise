class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        n = len(sequence)
        m = len(word)
        maxk=0
        OPT=[0 for i in range(n)]

        #if len(word)=2, check if seq[0,1 (inclusive)]=word (last index=1)
        #if len(word)=4, check if seq[0,1,2,3]=word (last index=3)
        #if len(word)=m, check seq from 0 to m-1 (last index=m-1)
        #start from the first possible index where 'word' can end 
        for i in range(m-1,n):
            if sequence[i-m+1: i+1]==word:
                if i-m>=0:
                    OPT[i] = OPT[i-m]+1
                else:
                    OPT[i]=1
                maxk = max(maxk, OPT[i])
            else:
                OPT[i]=0
        return maxk
