'''
1. Find anagram of 1st word
2. Add anagram to a dictionary d = {anagram:word}
3. Find anagram of 2nd word. If its same as key in dictionary, add word to its value list. Else add anagram as a different key in the dictionary
4. Return value pairs
'''

def compute_anagram(word):
    h = {}
    for i in range( len(word) ):
        h[word[i]] = h.get(word[i],0) + 1
    return h

class Solution(object):
    def groupAnagrams(self, strs):
        d = dict()

        for i in range( len(strs) ):
            a = compute_anagram(strs[i])
            key = tuple(sorted(a.items()))

            if key not in d:
                d[key] = [strs[i]]
            else:
                d[key].append(strs[i])

        return d.values()
            
