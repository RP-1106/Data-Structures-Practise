class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = {}
        for i in range(len(nums)):
            if target-nums[i] in hash:
                return [i, hash[target-nums[i]]]
            hash[nums[i]]=i