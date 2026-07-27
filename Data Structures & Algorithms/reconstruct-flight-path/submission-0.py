class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        tickets.sort(key=lambda p:p[0] + p[1], reverse=True)
        for u,v in tickets:
            adj[u].append(v)
        res = []
        def dfs(u):
            while adj[u]:
                dst = adj[u].pop()
                dfs(dst)
            res.append(u)
        dfs('JFK')
        return res[::-1]
        