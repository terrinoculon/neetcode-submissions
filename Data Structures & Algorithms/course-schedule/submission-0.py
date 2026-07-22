from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegrees = [0]*numCourses
        
        for u,v in prerequisites:
            graph[u].append(v)
            indegrees[v] += 1
        q = deque([i for i in range(numCourses) if indegrees[i] == 0])
        order = []
        while q:
            u = q.popleft()
            order.append(q)
            for v in graph[u]:
                indegrees[v]-=1
                if indegrees[v] == 0:
                    q.append(v)
        return len(order) == numCourses
