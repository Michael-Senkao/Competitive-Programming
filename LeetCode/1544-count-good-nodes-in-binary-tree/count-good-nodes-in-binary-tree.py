# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bfs(self,root):
        q = deque([(root, float('-inf'))])
        count = 0

        while q:
            node,max_v = q.popleft()
            new_max = max(max_v, node.val)
            count += (node.val == new_max)
            if node.left:
                q.append((node.left, new_max))
            if node.right:
                q.append((node.right, new_max))
        return count
        
    def goodNodes(self, root: TreeNode) -> int:
        return self.bfs(root)
        