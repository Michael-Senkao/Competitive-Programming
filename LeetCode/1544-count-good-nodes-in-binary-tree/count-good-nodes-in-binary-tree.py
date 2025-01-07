# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_v = float('-inf')

    def dfs(self,node):
        if node is None:
            return 0
        
        prev_max = self.max_v
        self.max_v = max(node.val, prev_max)
        count = 1 if self.max_v == node.val else 0
        count += self.dfs(node.left) + self.dfs(node.right)
        self.max_v = prev_max
        return count
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root)
        