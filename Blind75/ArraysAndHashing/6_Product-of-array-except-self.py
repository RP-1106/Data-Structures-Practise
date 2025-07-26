class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        s = [1]*n
        p = [1]*n
        res = [1]*n

        for i in range(1,n):
            p[i] = p[i-1]*nums[i-1]
            s[-i-1] = s[-i]*nums[-i]
        for i in range(n):
            res[i] = p[i]*s[i]
        return res