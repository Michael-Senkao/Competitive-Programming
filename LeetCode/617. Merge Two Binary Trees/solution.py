# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge(node1=None, node2=None):
            if node1 and node2:
                node1.val += node2.val
                node1.left = merge(node1.left, node2.left)
                node1.right = merge(node1.right, node2.right)
            elif node2:
                return node2
            return node1

        return merge(root1, root2)
