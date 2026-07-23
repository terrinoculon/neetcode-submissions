import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[-1])
        g0 = grid[0][0]
        pq = [(g0,0,0)]
        cost = {(0,0):g0}
        max_cost = g0
        while pq:
            w, r, c = heapq.heappop(pq)
            if r == R-1 and c==C-1:
                return w
            if w > cost.get((r,c), float('infinity')):
                continue
            for dr, dc in ((-1,0), (0,-1), (0,1), (1,0)):
                nr,nc = r+dr, c+dc
                if 0<=nr<R and 0<=nc<C:
                    dw = max(w, grid[nr][nc])
                    if dw<cost.get((nr,nc), float('infinity')):
                        heapq.heappush(pq,(dw,nr,nc))
                        cost[(nr,nc)] = dw
        return -1