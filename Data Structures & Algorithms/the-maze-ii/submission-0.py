class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        R, C = len(maze), len(maze[-1])
        pq = [(0,start[0],start[1])]
        cost = {(start[0],start[1]):0}
        total_cost = 0
        def add_tup(x,y,a):
            return x[0] + a*y[0], x[1]+a*y[1]
        def cost_in_dir(cur, d):
            cl = 0
            while True:
                cl+=1
                np = add_tup(cur,d,cl)
                if not(0<=np[0]<R and  0<=np[1]<C) or maze[np[0]][np[1]]:
                    return cl-1 
            return -1

        while pq:
            w, r, c = heapq.heappop(pq)
            
            if r == destination[0] and c == destination[1]:
                    return w
            if w > cost.get((r,c), float('infinity')):
                continue
            for direction in ((-1,0), (0,-1), (0,1), (1,0)):
                dw = cost_in_dir((r,c), direction)
                (nr,nc) = add_tup((r,c), direction, dw)
                
                if w+dw<cost.get((nr,nc), float('infinity')):
                    heapq.heappush(pq,(w+dw,nr,nc))
                    cost[(nr,nc)] = w+dw
        return -1