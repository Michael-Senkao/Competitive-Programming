# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_order = []

        def bfs(node, level):
            if node:
                if len(level_order) >= level:
                    level_order[level-1].append(node.val)
                else:
                    level_order.append([node.val])
                bfs(node.left, level +1)
                bfs(node.right, level+1)
        
        bfs(root, 1)
        for i in range(1, len(level_order), 2):
            level_order[i].reverse()
        return level_order