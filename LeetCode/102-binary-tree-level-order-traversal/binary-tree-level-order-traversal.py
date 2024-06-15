# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_order = []
        def dfs(node, current_level):
            if not node:
                return
            if len(level_order) < current_level + 1:
                level_order.append([node.val])
            else:
                level_order[current_level].append(node.val)
            dfs(node.left, current_level + 1)
            dfs(node.right, current_level + 1)
        
        dfs(root, 0)
        return level_order
        