def comp_anagram( i):
        count={}
        for j in i:
            count[j] = count.get(j,0)+1
        return count

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash = {}
        for i in strs:
            a = comp_anagram(i)
            key = tuple(sorted(a.items()))

            if key not in hash:
                hash[key] = [i]
            else:
                hash[key].append(i)
        return hash.values()

        