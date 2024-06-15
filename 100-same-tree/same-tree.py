# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traverse(a, b):
            if not a and not b:
                return True
            if a and b:
                return a.val == b.val and traverse(a.left, b.left) and traverse(a.right, b.right)
            return False
        
        return traverse(p, q)