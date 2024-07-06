# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def preorder(node):
            if not node:
                return ""
            left = preorder(node.left)
            right = preorder(node.right)
            res = str(node.val)
            
            if right:
                res += "(" + left+ ")" + "(" + right + ")"
            elif left:
                res += "(" + left+ ")"
            return res
        return preorder(root)