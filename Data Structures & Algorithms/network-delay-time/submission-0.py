import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        G = [[] for _ in range(n)]
        for u,v,t in times:
            G[u-1].append((v-1,t))
        pq = [(0,k-1)]
        cost={k-1:0}
        while pq:
            time, node = heapq.heappop(pq)
            if time > cost.get(node, float('infinity')):
                continue
            for neighbor, dt in G[node]:
                next_time = time + dt
                if next_time<cost.get(neighbor, float('infinity')):
                    heapq.heappush(pq,(next_time, neighbor))
                    cost[neighbor] = next_time
        
        if len(cost) < n:
            return -1
        return max(cost.values())