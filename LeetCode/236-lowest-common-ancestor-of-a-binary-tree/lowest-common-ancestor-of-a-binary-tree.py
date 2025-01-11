# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, node, target, path):
        if node is None:
            return False
        if node == target:
            path.append(node)
            return True
        if self.dfs(node.left, target, path) or self.dfs(node.right, target, path):
            path.append(node)
            
            return True
        return False
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path1 = []
        path2 = []
        self.dfs(root, p, path1)
        self.dfs(root, q, path2)
        # print(path1, path2)

        i = len(path1) - 1
        j = len(path2) - 1
        while i >= 0 and j >= 0 and path1[i] == path2[j]:
            i -= 1
            j -= 1
        
            
        return path1[i+1]