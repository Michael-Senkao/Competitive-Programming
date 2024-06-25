# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        def helper(node):
            if not node:
                return
            nonlocal currSum
            helper(node.right)
            currSum+= node.val
            node.val = currSum
            helper(node.left)
        
        currSum = 0
        helper(root)
        
        return root