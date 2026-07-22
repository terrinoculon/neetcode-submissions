class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        states = [0]*numCourses
        graph = [[] for _ in range(numCourses)]        
        
        for u,v in prerequisites:
            graph[u].append(v)

        def dfs(node):
            if states[node] == 1:
                return True
            if states[node] == 2:
                return False
            states[node] = 1
            for v in graph[node]:
                if dfs(v):
                    return True
            states[node] = 2
            return False
        
        for i in range(numCourses):
            if states[i] == 0 and dfs(i):
                return False
        return True
