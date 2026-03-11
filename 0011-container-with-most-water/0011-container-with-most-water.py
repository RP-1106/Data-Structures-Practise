class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l=0
        r=len(height)-1

        max_amt = 0
        while l<r:
            h = min(height[l], height[r])
            w = abs(l-r)
            max_amt = max(max_amt, h*w)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_amt