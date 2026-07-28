# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        qu = deque([(p,q)])
        while qu:
            a, b = qu.popleft()
            if (a is None) != (b is None):
                return False
            if (a is None) and (b is None):
                continue
            if a.val!=b.val:
                return False

            qu.append((a.left,b.left))
            qu.append((a.right, b.right))
        return True