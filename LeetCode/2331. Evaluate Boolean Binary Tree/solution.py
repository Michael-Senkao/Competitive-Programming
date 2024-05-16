# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node)->bool:
        if node.val == 0:
            return False
        if node.val == 1:
            return True
        
        
        if node.left and node.right:
            if node.val == 2:
                return self.dfs(node.left) or self.dfs(node.right)
            else:
                return self.dfs(node.left) and self.dfs(node.right)
        if node.left:
            return self.dfs(node.left)
        if node.right:
            return self.dfs(node.right)

    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)
        
