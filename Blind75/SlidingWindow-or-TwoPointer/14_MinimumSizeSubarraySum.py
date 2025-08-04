class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        if target in nums:
            return 1
        if sum(nums)<target:
            return 0
        else:
            l=0
            csum=0
            minLen=float('Inf')
            for r in range(len(nums)):
                csum+=nums[r]
                while csum>=target:
                    minLen = min(minLen,r-l+1)
                    csum-=nums[l]
                    l+=1
            
            if minLen==float('Inf'):
                return 0
            else:
                return minLen
