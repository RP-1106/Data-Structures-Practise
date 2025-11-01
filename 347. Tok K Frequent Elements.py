class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}
        freq = [ [] for i in range(len(nums)+1)]

        for i in nums:
            count[i]=count.get(i,0)+1
        for (key,v) in count.items():
            freq[v].append(key)

        res = []
        for j in range(len(freq)-1,-1,-1):
            for m in freq[j]:
                res.append(m)

                if len(res)==k:
                    return res



        
