class Solution:
    def threeSum(self, nums) :
        res=[]
        nums.sort()

        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            if nums[i]>0:
                break
            l=i+1
            r=len(nums)-1

            while l<r:
                if nums[i]+nums[l]+nums[r]==0:
                    if [nums[i],nums[l],nums[r]] not in res:
                        res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                elif nums[i]+nums[l]+nums[r]<0:
                    l+=1
                elif nums[i]+nums[l]+nums[r]>0:
                    r-=1

        return res
                