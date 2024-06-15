# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(node, min_val, max_val):
            if not node:
                return True
            if not(min_val < node.val < max_val):
                return False
            return traverse(node.left, min_val, node.val) and traverse(node.right, node.val, max_val)

        return traverse(root, float('inf')*-1, float('inf'))