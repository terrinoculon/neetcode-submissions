class DSU:
    def __init__(self,n):
            self.parent = list(range(n))
            self.rank = [0]*n
    def find(self, node):
        if self.parent[node]!=node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    def union(self,x,y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx]<self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[ry]<self.rank[rx]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx]+=1
        return True
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i+1,n):
                dist = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                edges.append((dist, i, j))
        edges.sort()
        dsu = DSU(n)
        total_cost = 0
        for d,u,v in edges:
            if dsu.union(u,v):
                total_cost += d
        return total_cost
