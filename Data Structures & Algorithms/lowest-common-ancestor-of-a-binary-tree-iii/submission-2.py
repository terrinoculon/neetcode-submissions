"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def height(node):
            h = 0
            while node:
                h+=1
                node = node.parent
            return h
        p_h = height(p)
        q_h = height(q)
        if p_h<q_h:
            q,p = p,q
        diff = abs(p_h-q_h)
        while diff:
            p = p.parent
            diff-=1
        while p!=q:
            p = p.parent
            q = q.parent
        return p
