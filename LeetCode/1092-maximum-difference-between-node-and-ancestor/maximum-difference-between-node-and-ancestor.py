# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(node, maximum, minimum):
            if not node:
                return maximum - minimum
            if node.val < minimum:
                minimum = node.val
            if node.val > maximum:
                maximum = node.val
            left_difference = helper(node.left, maximum, minimum)
            right_difference = helper(node.right, maximum, minimum)

            return max(left_difference, right_difference)
    
        return helper(root, root.val, root.val)