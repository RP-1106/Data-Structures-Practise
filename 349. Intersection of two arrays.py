class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()

        l=0
        r=0
        new=set()
        
        while l<len(nums1) and r<len(nums2):
            if nums1[l]==nums2[r]:
                new.add(nums1[l])
                l+=1
                r+=1

            elif nums1[l]>nums2[r]:
                r+=1

            elif nums1[l]<nums2[r]:
                l+=1
        return list(new)

        
