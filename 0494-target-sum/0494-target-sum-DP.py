class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        s = sum(nums)
        n = len(nums)
        if (target+s)%2!=0:
            return 0
        if abs(target)>s:
            return 0

        new=(s+target)//2

        OPT=[[0 for j in range(new+1)] for i in range(n+1)]
        
        #how many ways can one mark a target sum of zero using array of different length = 1 (using empty subset {})
        for i in range(n+1):
            OPT[i][0]=1

        for i in range(1,n+1):
            for t in range(new+1):
                if t<nums[i-1]:
                    OPT[i][t]=OPT[i-1][t]
                else:
                    OPT[i][t]=OPT[i-1][t]+OPT[i-1][t-nums[i-1]]
        return OPT[n][new]

        


        