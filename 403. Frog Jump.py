class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if len(stones)<2 or stones[1]!=stones[0]+1:
            return False

        #INDICE = {STONE i: INDEX OF STONE i}
        indice={}
        for i in range(len(stones)):
            indice[stones[i]]=i

        stone=set()
        for i in stones:
            stone.add(i)

        #create memoized array for true/false
        n=len(stones)
        OPT=[[False for j in range(n)] for i in range(n)]
        OPT[1][1]=True

        for i in range(1,n):
            for j in range(n):
                if OPT[i][j] is True:
                    if j-1>0 and stones[i]+(j-1) in stone:
                        OPT[indice[stones[i]+(j-1)]][j-1]=True
                    if stones[i]+(j) in stone:
                        OPT[indice[stones[i]+(j)]][j]=True
                    if j+1<n and stones[i]+(j+1) in stone:
                        OPT[indice[stones[i]+(j+1)]][j+1]=True
                else:
                    continue
        if True in OPT[n-1]:
            return True
        else:
            return False
                    
