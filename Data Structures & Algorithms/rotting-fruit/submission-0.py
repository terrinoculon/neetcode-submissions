from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        q = deque([])
        R, C = len(grid), len(grid[-1])
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    fresh +=1
                elif grid[i][j] == 2:
                    q.append((i,j, 0))
        t = 0
        while q:
            r, c, t = q.popleft()
            for dr, dc in ((-1,0), (0,-1), (0,1), (1,0)):
                nr, nc = r + dr, c + dc
                if 0<=nr<R and 0 <=nc<C and grid[nr][nc] == 1:
                    q.append((nr,nc, t + 1))
                    grid[nr][nc] = 2
                    fresh -=1
            
        return t if fresh == 0 else -1
        