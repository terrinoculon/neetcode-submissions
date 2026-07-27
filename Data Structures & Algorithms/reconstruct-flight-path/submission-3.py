class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        tickets.sort( reverse=True)
        for u,v in tickets:
            adj[u].append(v)
        res = []
        def dfs(u):
            while adj[u]:
                dfs(adj[u].pop())                
            res.append(u)
        dfs('JFK')
        return res[::-1]
        