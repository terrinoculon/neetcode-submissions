class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parents = list(range(n))
        rank = [0]*n
        components = n
        def find(x):
            if parents[x]!=x:
                parents[x] = find(parents[x])
            return parents[x]
        def union(x,y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            if rank[rx]<rank[ry]:
                parents[rx] = ry
            else:
                parents[ry] = rx
                if rank[rx] == rank[ry]:
                    rank[ry] +=1
            return True
        for u,v in edges:
            if not union(u,v):
                return False
            components-=1
        print(components)
        return components == 1