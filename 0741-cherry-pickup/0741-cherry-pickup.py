class Solution(object):
    def cherryPickup(self, grid):
        n = len(grid)
        if grid[n-1][n-1] == -1 or grid[0][0] == -1:
            return 0

        # Single OPT array, initialize with -1
        OPT = [[[-1 for z in range(n)] for j in range(n)] for i in range(n)]
        
        def solve(r1, c1, r2):
            c2 = r1 + c1 - r2
            
            # Out of bounds or obstacle
            if r1 >= n or c1 >= n or r2 >= n or c2 >= n or c2 < 0:
                return float('-inf')
            if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float('-inf')
            
            # Base case: reached destination
            if r1 == n-1 and c1 == n-1:
                return grid[r1][c1]
            
            # Memoization check
            if OPT[r1][c1][r2] != -1:
                return OPT[r1][c1][r2]
            
            # Collect cherries at current position
            cherries = grid[r1][c1]
            if r1 != r2 or c1 != c2:
                cherries += grid[r2][c2]
            
            # Try all 4 moves (these will be computed first via recursion)
            maxCherries = max(
                solve(r1+1, c1, r2+1),
                solve(r1+1, c1, r2),
                solve(r1, c1+1, r2+1),
                solve(r1, c1+1, r2)
            )
            
            # Store result
            OPT[r1][c1][r2] = cherries + maxCherries if maxCherries != float('-inf') else float('-inf')
            return OPT[r1][c1][r2]
        
        result = solve(0, 0, 0)
        return max(0, result)