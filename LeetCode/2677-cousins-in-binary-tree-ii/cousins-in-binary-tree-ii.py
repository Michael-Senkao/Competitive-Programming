# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level_sums = []
        q = deque()
        q.append(root)
        
        # Find level sum using inorder traversal
        while q:
            level_sum = 0
            for _ in range(len(q)):
                curr_node = q.popleft()
                level_sum += curr_node.val
                if curr_node.left:
                    q.append(curr_node.left)

                if curr_node.right:
                    q.append(curr_node.right)

            level_sums.append(level_sum)

        # Update the tree values
        q.append(root)
        i = 0
        while q:
            for _ in range(len(q)):
                curr_node = q.popleft()
                curr_node.val = level_sums[i] - curr_node.val

                if curr_node.left:
                    if curr_node.right:
                        curr_node.left.val += curr_node.right.val
                        curr_node.right.val = curr_node.left.val
                        q.append(curr_node.right)

                    q.append(curr_node.left)
                elif curr_node.right:
                    q.append(curr_node.right)
            
            i += 1

            
        return root