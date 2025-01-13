# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findRoot(self, node, target):

        if node is None:
            return 
        if node.val > target:
            return self.findRoot(node.left, target)
        if node.val < target:
            return self.findRoot(node.right, target)
        return node


    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        return self.findRoot(root, val)
        
        
        