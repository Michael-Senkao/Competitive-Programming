# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node is not None:
                if node.left:
                    dfs(node.left)
                    dfs(node.right)
                elif node.right:
                    dfs(node.right)
                else:
                    leaves1.append(node.val)

        leaves1 = []

        dfs(root1)

        stack = [root2]
        i = 0
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            elif node.left:
                stack.append(node.left)
            elif i < len(leaves1) and node.val == leaves1[i]:
                i += 1
            else:
                return False
        return i == len(leaves1)