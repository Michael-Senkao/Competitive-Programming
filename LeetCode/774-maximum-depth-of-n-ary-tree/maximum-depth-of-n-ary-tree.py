"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        def dfs(node, depth):
            if not node:
                return depth
            maxDepth = depth + 1
            for child in node.children:
                maxDepth = max(maxDepth, dfs(child, depth + 1))
            return maxDepth
        
        if not root:
            return 0

        return dfs(root, 0)