class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        OPT=[float('inf') for i in range(n)]
        OPT[0]=cost[0]
        OPT[1]=cost[1]

        for i in range(2,n):
            OPT[i]=cost[i]+min(OPT[i-1],OPT[i-2])
        return min(OPT[n-1],OPT[n-2])            
        