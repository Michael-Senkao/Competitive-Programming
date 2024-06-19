# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, currSum):
            currSum += node.val
            
            if node.left and node.right:
                return dfs(node.left, currSum) or dfs(node.right, currSum)
            if node.left:
                return dfs(node.left, currSum)
            if node.right:
                return dfs(node.right, currSum)
            return currSum == targetSum 

        if not root:
            return False
        return dfs(root, 0)           