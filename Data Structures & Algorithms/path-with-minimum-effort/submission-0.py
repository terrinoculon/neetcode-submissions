import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        R, C = len(heights), len(heights[-1])
        pq = [(0,0,0)]
        cost = {(0,0):0}
        while pq:
            w, r, c = heapq.heappop(pq)
            if r==R-1 and c == C-1:
                return w
            if w>cost.get((r,c), float('infinity')):
                continue
            for dr, dc in ((-1,0), (0,-1), (1,0), (0,1)):
                nr, nc = dr  + r, dc + c
                
                if 0<=nr<R and 0<=nc<C:
                    dw =max(w, abs(heights[nr][nc] - heights[r][c]))
                    
                    if cost.get((nr,nc), float('infinity'))> dw:
                        heapq.heappush(pq, (dw,nr,nc))
                        cost[(nr,nc)] = dw
        return -1