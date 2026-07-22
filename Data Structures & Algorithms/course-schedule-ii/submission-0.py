from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indeg = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        for v, u in prerequisites:
            graph[u].append(v)
            indeg[v] +=1
        q = deque([u for u in range(numCourses) if indeg[u] == 0])
        order = []
        while q:
            u = q.popleft()
            order.append(u)
            for v in graph[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        return order if len(order) == numCourses else []
