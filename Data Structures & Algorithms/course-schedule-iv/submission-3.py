class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        indeg = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        for  u, v in prerequisites:
            graph[u].append(v)
            indeg[v] +=1
        isPrereq = [set() for _ in range(numCourses)]
        q = deque([u for u in range(numCourses) if indeg[u] == 0])
        while q:
            u = q.popleft()
            for v in graph[u]:
                isPrereq[v].add(u)
                isPrereq[v].update(isPrereq[u])
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        return [u in isPrereq[v] for u,v in queries]
