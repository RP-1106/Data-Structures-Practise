class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        n = len(arr)
        new_max=float('inf')*-1
        new=[float('inf')*-1]*(n)
        for i in range(n-1,0,-1):
            new_max = max(new_max, arr[i])
            new[i] = new_max
            #print(new)
        new.pop(0)
        new.append(-1)
        return new
        