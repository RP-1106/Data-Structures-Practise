class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.append(0)
        n = len(cost)
        OPT=[float('inf') for i in range(n+1)]
        OPT[0]=0
        OPT[1]=cost[0]

        for i in range(2,n+1):
            OPT[i]=cost[i-1]+min(OPT[i-1],OPT[i-2])
        return OPT[n]
            
        