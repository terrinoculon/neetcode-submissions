class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31-1
        R, C = len(grid), len(grid[-1])
        q = deque([])
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    q.append((r,c,0))
        while q:
            r,c,d = q.popleft()
            for dr,dc in ((-1,0),(0,-1), (1,0),(0,1)):
                nr,nc = r+dr, c + dc
                if 0<=nr<R and 0<=nc<C and grid[nr][nc]==INF:
                    grid[nr][nc] = d+1
                    q.append((nr,nc, d+1))
        return