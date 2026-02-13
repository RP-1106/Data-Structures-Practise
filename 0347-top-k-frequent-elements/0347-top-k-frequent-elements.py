class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        num_to_freq = {}
        for i in nums:
            num_to_freq[i] = num_to_freq.get(i,0)+1
        
        freq_to_num = defaultdict(list)
        for i in num_to_freq:
            if num_to_freq[i] not in freq_to_num:
                freq_to_num[num_to_freq[i]] =  [i]
            else:
                freq_to_num[num_to_freq[i]].append(i)
        
        result=[]
        for i in range(len(nums),-1,-1):
            if i in freq_to_num:
                for j in freq_to_num[i]:
                    result.append(j)
                    if len(result)==k:
                        return result
            


        
                

        

        