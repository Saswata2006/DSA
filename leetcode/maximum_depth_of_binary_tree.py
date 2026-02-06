# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        arr = []
        def sol(i):
            if i == None:
                return 0
            return 1 + max(sol(i.right),sol(i.left))
        return sol(root)