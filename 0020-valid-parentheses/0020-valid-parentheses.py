class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        '''
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
        '''

        d = {"]":"[", "}":"{", ")":"("}
        stack=[]


        for i in s:
            if i=="[" or i=="{" or i=="(":
                stack.append(i)
            if i=="]" or i=="}" or i==")":
                if len(stack)==0:
                    return False
                if stack[-1]==d[i]:
                    stack.pop(-1)
                else:
                    return False
        if len(stack)==0:
            return True
        else:
            return False


        
        