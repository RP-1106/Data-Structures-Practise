class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        symbols = {"]":"[", "}":"{", ")":"("}

        for i in s:
            if i in symbols:
                if stack and stack[-1]==symbols[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False


        
        
