class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[-1])
        max_area = 0 
        def dfs(r,c, area):
            area += 1
            grid[r][c] = 2
            for dr, dc in ((-1,0), (0,-1), (1,0), (0,1)):
                nr, nc = r + dr, c + dc
                if 0<=nr<R and 0<=nc<C and grid[nr][nc] == 1:
                    area = dfs(nr,nc, area)
            return area
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    max_area = max(dfs(i,j,0), max_area)
        return max_area
        
