class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        n = len(sequence)
        m = len(word)

        OPT = [0 for i in range(n)]

        for i in range(m-1,n):
            if sequence[i-m+1:i+1]==word:
                if i-m+1==0:
                    OPT[i]=1
                else:
                    OPT[i]=OPT[i-m]+1
        return max(OPT)