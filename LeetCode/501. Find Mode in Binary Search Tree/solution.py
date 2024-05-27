# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def count(node):
            if not node:
                return

            freq[node.val] += 1
            count(node.left)
            count(node.right)
       

        freq = defaultdict(int)
        count(root)
        mode_count = max(freq.values()) 
        res = []

        for x in freq:
            if freq[x] == mode_count:
                res.append(x)
        
        return res
