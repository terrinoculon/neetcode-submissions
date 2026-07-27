class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        G = [[] for _ in range(n)]
        for u,v, w in flights:
            G[u].append((v,w))
        cost = {(src,k+1):0}
        pq = [(0,src,k+1)]
        
        while pq:
            w,u, rem  = heapq.heappop(pq)
            if u == dst:
                return w
            if w > cost.get((u, rem), float('infinity')) or rem == 0:
                continue
            for v, dw in G[u]:
                nw = w+dw
                if nw<cost.get((v,rem-1), float('infinity')) : 
                    heapq.heappush(pq, (nw, v, rem-1))
                    cost[(v,rem-1)] = nw
        return -1