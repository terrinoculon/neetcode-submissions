class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R,C = len(heights), len(heights[-1])
        atlantic = [[False]*C for _ in range(R)]
        pacific = [[False]*C for _ in range(R)]
        pac_srcs = []
        atl_srcs = []
        for r in range(R):
            pac_srcs.append((r,0))
            atl_srcs.append((r, C-1))
        for c in range(C):
            pac_srcs.append((0,c))
            atl_srcs.append((R-1,c))
        def bfs(sources, flags):
            q = deque(sources)
            while q:
                r,c = q.popleft()
                flags[r][c] = True
                for dr,dc in ((-1,0), (0,-1), (1, 0), (0,1)):
                    nr, nc = r + dr, c + dc
                    if 0<=nr<R and 0<=nc<C and not flags[nr][nc] and heights[nr][nc]>=heights[r][c]:
                        q.append((nr,nc))
        bfs(pac_srcs, pacific)
        bfs(atl_srcs, atlantic)
        out = []
        for i in range(R):
            for j in range(C):
                if atlantic[i][j] and pacific[i][j]:
                    out.append([i,j])
        return out