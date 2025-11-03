class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        output=[]
        def get_binary(num):
            binary = ""
            while num > 0:
                binary = str(num % 2) + binary
                num = num // 2
            return binary or "0"

        for i in range(n+1):
            count=0
            bnum=get_binary(i)
            for j in bnum:
                if j=="1":
                    count+=1
            output.append(count)
        return output


        