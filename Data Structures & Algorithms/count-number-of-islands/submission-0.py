class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[-1])
        seen = set()
        def dfs(r,c):
            seen.add((r,c))
            for dr,dc in ((-1,0), (0,-1), (0,1), (1,0)):
                nr, nc = r + dr, c + dc
                if 0<=nr<R and 0<=nc<C and grid[nr][nc]=="1" and (nr, nc) not in seen:
                    # seen.add((nr, nc))
                    dfs(nr,nc)
            return
        count = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == "1" and (i,j) not in seen:
                    count +=1
                    dfs(i,j)
        return count