class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def isPalindromeRange(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                # Try skipping either s[l] or s[r]
                return isPalindromeRange(l + 1, r) or isPalindromeRange(l, r - 1)
            l += 1
            r -= 1

        return True
