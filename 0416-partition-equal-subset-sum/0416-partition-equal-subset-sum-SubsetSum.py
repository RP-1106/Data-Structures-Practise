class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums)%2!=0:
            return False
        k = sum(nums)
        n = len(nums)
        t = (k/2)
        OPT=[[False for j in range(t+1)] for i in range(n+1)]
        for i in range(t+1):
            OPT[0][i]=False

        for i in range(t+1):
            if nums[0]==i:
                OPT[1][i] = True
            else:
                OPT[1][i] = False

        for i in range(2,n+1):
            for j in range(t+1):
                if j<nums[i-1]:
                    OPT[i][j] = OPT[i-1][j]
                else:
                    OPT[i][j]=OPT[i-1][j] or OPT[i-1][j-nums[i-1]]
        return OPT[n][t]

        
