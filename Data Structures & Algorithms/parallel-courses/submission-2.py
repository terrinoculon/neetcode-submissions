class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        indeg = [0] * n
        height = 0
        graph = [[] for _ in range(n)]
        for v, u in relations:
            graph[u-1].append(v-1)
            indeg[v-1] +=1
        q = deque([(u,1) for u in range(n) if indeg[u] == 0])
        order = []
        while q:
            u,d = q.popleft()
            order.append(u)
            height = max(d, height)
            for v in graph[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append((v, d+1))
        return height if len(order) == n else -1
