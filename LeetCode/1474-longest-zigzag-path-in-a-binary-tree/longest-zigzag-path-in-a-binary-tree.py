# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, node, isLeft):
        if node is None:
            return 0
        
        left,right = 0,0
        if isLeft:
            left = self.solve(node.right, False) + 1
            right = self.solve(node.left, True)
            

            self.ans = max(self.ans, left, right)
            # print(left,right, self.ans)
            return left
        else:
            right = self.solve(node.left, True) + 1
            left = self.solve(node.right, False)

            self.ans = max(self.ans, left, right)
            # print(left,right, self.ans)
            return right


    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        self.solve(root.left, True)
        # print(self.ans)
        self.solve(root.right, False)
        # print(self.ans)
        return self.ans