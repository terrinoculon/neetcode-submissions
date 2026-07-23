class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        G = [[] for _ in range(n)]
        for (u,v), p in zip(edges, succProb):
            G[u].append((v,p))
            G[v].append((u,p))
        cost = [float('infinity')]*n
        pq =[(-1,start_node)]
        while pq:
            p, u = heapq.heappop(pq)
            if u == end_node:
                return -p
            if p>cost[u]:
                continue
            for v, pv in G[u]:
                if p*pv < cost[v]:
                    heapq.heappush(pq,(p*pv, v))
                    cost[v] = p*pv
        return 0