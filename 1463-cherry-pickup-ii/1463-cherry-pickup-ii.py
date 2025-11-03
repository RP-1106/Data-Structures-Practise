class Solution(object):
    def cherryPickup(self, grid):
        r = len(grid)
        c = len(grid[0])
        
        if r == 1:
            if c == 1:
                return grid[0][0]
            else:
                return grid[0][0] + grid[0][c-1]

        OPT = [[[None for _ in range(c)] for _ in range(c)] for _ in range(r)]
        
        def solve(r1, c1, c2):
            if r1 >= r or c1 >= c or c2 >= c or c2 < 0 or c1 < 0:
                return float('-inf')
        
            if r1 == r - 1:
                if c1 == c2:
                    return grid[r1][c1]
                else:
                    return grid[r1][c1] + grid[r1][c2]
            
            # Memoization check
            if OPT[r1][c1][c2] is not None:
                return OPT[r1][c1][c2]
            
            # Calculate current cherries
            if c1 == c2:
                cherries = grid[r1][c1]
            else:
                cherries = grid[r1][c1] + grid[r1][c2]

            max_future = float('-inf')
            for dc1 in [-1, 0, 1]:      # Alice's next column move
                for dc2 in [-1, 0, 1]:  # Bob's next column move
                    max_future = max(max_future, solve(r1 + 1, c1 + dc1, c2 + dc2))
            OPT[r1][c1][c2] = cherries + max_future
            return OPT[r1][c1][c2]

        result = solve(0, 0, c - 1)
        return max(0, result)