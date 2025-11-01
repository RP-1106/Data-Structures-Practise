class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict

        count = 0
        curr_sum = 0
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1  # To handle the case where subarray starts at index 0

        for num in nums:
            curr_sum += num
            if curr_sum - k in prefix_sums:
                count += prefix_sums[curr_sum - k]
            prefix_sums[curr_sum] += 1

        return count
