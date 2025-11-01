class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def house_robber(nums):
            n=len(nums)
            OPT=[-1]*(n+1)
            OPT[0]=0
            OPT[1]=nums[0]

            for i in range(2,n+1):
                OPT[i]=max(OPT[i-1], OPT[i-2]+nums[i-1])
            return OPT[n]

        if len(nums)==1:
            return nums[0]
        else:
            case1 = house_robber(nums[:-1])
            case2 = house_robber(nums[1:])
            return max(case1, case2)
        
        
