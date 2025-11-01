class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        OPT=[-1]*(n+1)
        OPT[0]=0
        OPT[1]=nums[0]

        for i in range(2,n+1):
            OPT[i]=max(nums[i-1]+OPT[i-2], OPT[i-1])
        return OPT[n]
