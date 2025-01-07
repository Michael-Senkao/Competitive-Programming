# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,node, curr_max):
        if node is None:
            return 0
        new_max = max(node.val, curr_max)
        return (1 if new_max==node.val else 0) + self.dfs(node.left, new_max) + self.dfs(node.right, new_max)
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, float('-inf'))
        