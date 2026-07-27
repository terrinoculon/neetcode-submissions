class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R, C = len(board), len(board[-1])
        sources = []
        for i in range(R):
            if board[i][0] == 'O':
                sources.append((i,0))
            if board[i][C-1] == 'O':
                sources.append((i,C-1))
        for i in range(C):
            if board[0][i] == 'O':
                sources.append((0,i))
            if board[R-1][i] == 'O':
                sources.append((R-1,i))
        
        seen = set(sources)
        q = deque(sources)
        while q:
            r,c = q.popleft()
            for dr,dc in ((-1,0), (0,-1), (1,0), (0,1)):
                nr, nc = r +dr, c + dc
                if 0<=nr<R and 0<=nc<C and (nr,nc) not in seen and board[nr][nc]=='O':
                    q.append((nr,nc))
                    seen.add((nr,nc))
        for i in range(R):
            for j in range(C):
                if board[i][j] == 'O' and (i,j) not in seen:
                    board[i][j] = 'X'