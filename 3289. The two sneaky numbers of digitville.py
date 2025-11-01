class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[]
        numset=set()
        for i in nums:
            if i not in numset:
                numset.add(i)
            else:
                result.append(i)
        return result

        
