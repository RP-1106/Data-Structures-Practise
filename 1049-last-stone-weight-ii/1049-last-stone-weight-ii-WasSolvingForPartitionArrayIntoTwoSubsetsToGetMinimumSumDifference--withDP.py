class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        t = sum(stones)
        n = len(stones)
        OPT=[[False for j in range(t+1)] for i in range(n+1)]

        for target in range(t+1):
            if stones[0]==target:
                OPT[1][target]=True

        for i in range(2,n+1):
            for target in range(1,t+1):
                if target<stones[i-1]:
                    OPT[i][target]=OPT[i-1][target]
                else:
                    OPT[i][target]=OPT[i-1][target] or OPT[i-1][target-stones[i-1]]
        
        s1 = []
        for i in range(t+1):
            if OPT[n][i]==True:
                s1.append(i)

        s2 = []
        for i in range(len(s1)):
            s2.append(t-s1[i])

        min_diff = float('inf')
        for i in range(len(s1)):
            min_diff=min(min_diff, abs(s1[i]-s2[i]))

        return min_diff


        