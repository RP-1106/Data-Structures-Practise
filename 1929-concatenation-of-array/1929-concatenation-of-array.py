class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        twice = 2*n
        ans=[float('inf')]*twice
        for i in range(twice):
            if i<n:
                ans[i] = nums[i]
            else:
                ans[i] = nums[i-n]
        return ans

        