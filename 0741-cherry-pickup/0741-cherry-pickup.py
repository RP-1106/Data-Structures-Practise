class Solution(object):
    def cherryPickup(self, grid):
        n = len(grid)
        if grid[n-1][n-1] == -1 or grid[0][0] == -1:
            return 0

        OPT = [[[None for z in range(n)] for j in range(n)] for i in range(n)]
        
        def getValue(r1, c1, r2):
            c2 = r1 + c1 - r2
            if r1 >= n or c1 >= n or r2 >= n or c2 >= n or r2 < 0 or c2 < 0:
                return float('-inf')
            if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float('-inf')
            if OPT[r1][c1][r2] is not None:
                return OPT[r1][c1][r2]
            if r1 == n-1 and c1 == n-1:
                OPT[r1][c1][r2] = grid[r1][c1]
                return OPT[r1][c1][r2]
        
            if r1 == r2 and c1 == c2:
                cherries = grid[r1][c1]
            else:
                cherries = grid[r1][c1] + grid[r2][c2]
            
            # RECURSIVE RELATION 
            option1 = getValue(r1 + 1, c1, r2 + 1) #down,down
            option2 = getValue(r1 + 1, c1, r2) #down,right
            option3 = getValue(r1, c1 + 1, r2 + 1)#right,down
            option4 = getValue(r1, c1 + 1, r2) #right,right
            maxCherries = max(option1, option2, option3, option4)
            
            if maxCherries == float('-inf'):
                OPT[r1][c1][r2] = float('-inf')
            else:
                OPT[r1][c1][r2] = cherries + maxCherries
            return OPT[r1][c1][r2]

        result = getValue(0, 0, 0)
        return max(0, result) #zero due to unreachable