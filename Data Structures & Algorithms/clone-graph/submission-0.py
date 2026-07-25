"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None
        q=deque([node])
        d = {node:Node(node.val)}
        while q:
            u =q.popleft()
            
            for v in u.neighbors :
                if v not in d:
                    d[v]=Node(v.val)
                    q.append(v)
                d[u].neighbors.append(d[v])
        return d[node]

        