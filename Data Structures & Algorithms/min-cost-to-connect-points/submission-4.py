import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
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
            for i in range(n):
                d = abs(points[node][0] - points[i][0]) +  abs(points[node][1] - points[i][1])
                if not visited[i]:
                    heapq.heappush(pq,(d, i, node))
                
        return total_cost
