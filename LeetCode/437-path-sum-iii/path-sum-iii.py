# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, currSum, target, sums):
        if node is None:
            return 0
        currSum += node.val
        count = 0
        if currSum - target in sums:
            count += sums[currSum - target]
        sums[currSum] += 1
        count += self.dfs(node.left, currSum, target, sums) + self.dfs(node.right, currSum, target, sums)
        sums[currSum] -= 1
        return count
       
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        sums = defaultdict(int)
        sums[0] = 1

        return self.dfs(root, 0, targetSum, sums)

    