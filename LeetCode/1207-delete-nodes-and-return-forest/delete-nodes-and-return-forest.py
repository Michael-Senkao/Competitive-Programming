# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        def dfs(node):
            if not node:
                return None
            if node.val in delete:
                left = dfs(node.left)
                right = dfs(node.right)
                if left: 
                    res.append(left)
                if right: 
                    res.append(right)
                return None
            else:
                node.left = dfs(node.left)
                node.right = dfs(node.right)
                return node

        delete = set(to_delete)
        res = []
        root = dfs(root)
        if root:
            res.append(root)
        
        return res