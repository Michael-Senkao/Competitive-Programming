# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        def helper(node, parent_sum):
            if not node:
                return 0
            right_sum = helper(node.right, parent_sum)
            temp = node.val
            node.val = node.val + right_sum + parent_sum
            left_sum = helper(node.left, node.val)
            return temp + left_sum + right_sum
        
        helper(root, 0)
        return root