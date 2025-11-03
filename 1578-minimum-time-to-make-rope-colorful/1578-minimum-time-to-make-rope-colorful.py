class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        output=0
        n=len(colors)
        stack=[(colors[0],0)]
        for i in range(1,n):
            if stack[-1][0]==colors[i]:
                if neededTime[stack[-1][1]]<=neededTime[i]:
                    color,index = stack.pop(-1)
                    output+=neededTime[index]
                    stack.append((colors[i],i))
                else:
                   output+=neededTime[i]
            else:
                stack.append((colors[i],i))
        return output
                

                


        