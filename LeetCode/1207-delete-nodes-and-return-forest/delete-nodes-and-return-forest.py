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

            left = dfs(node.left)
            right = dfs(node.right)
            if node.val not in delete:
                node.left = left
                node.right = right
                return node
            else:
                if left:
                    res.append(left)
                if right:
                    res.append(right)
                return None

        delete = set(to_delete)
        res = []
        root = dfs(root)
        if root:
            res.append(root)
        
        return res