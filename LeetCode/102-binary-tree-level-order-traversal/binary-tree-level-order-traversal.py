# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        res = []

        q = deque()
        q.append((root, 1))

        while q:
            curr,level = q.popleft()
            if level > len(res):
                res.append([curr.val])
            else:
                res[level-1].append(curr.val)
            if curr.left:
                q.append((curr.left, level + 1))
            if curr.right:
                q.append((curr.right, level+1))

        return res
