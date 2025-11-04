class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        if word not in sequence:
            return 0

        n = len(sequence)
        m = len(word)
        OPT=0
        
        for i in range(1, n+1):
            if (word*i) in sequence:
                OPT+=1
            else:
                break
        return OPT
        