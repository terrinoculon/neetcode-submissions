import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        G = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                dist = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                G[i].append((j, dist))
                G[j].append((i, dist))
        pq = [(0,0,-1)]
        visited = [False] * n
        total_cost = 0
        mst = []
        while pq:
            dist, node, parent = heapq.heappop(pq)
            if visited[node]:
                continue
            visited[node] = True
            if parent != -1:
                mst.append((parent, node))
            total_cost += dist
            for neighbor, d in G[node]:
                if not visited[neighbor]:
                    heapq.heappush(pq,(d, neighbor, node))
                
        return total_cost
