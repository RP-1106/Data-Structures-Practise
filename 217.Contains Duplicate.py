class Solution(object):
    def containsDuplicate(self, nums):
        seen=set(nums)
        if len(seen)<len(nums):
            return True
        return False
        
