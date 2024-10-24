# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False


        q1 = deque([root1])
        q2 = deque([root2])

        while q1 and q2:
            x = q1.popleft()
            y = q2.popleft()

            left1 = x.left.val if x.left else -1
            left2 = y.left.val if y.left else -1
            right1 = x.right.val if x.right else -1
            right2 = y.right.val if y.right else -1

            if left1 == left2:
                if left1 != -1:
                    q1.append(x.left)
                    q2.append(y.left)
                if right1 == right2:
                    if right1 != -1:
                        q1.append(x.right)
                        q2.append(y.right)
                else:
                    return False
            elif left1 == right2:
                if left1 != -1:
                    q1.append(x.left)
                    q2.append(y.right)
                if right1 == left2:
                    if left2 != -1:
                        q1.append(x.right)
                        q2.append(y.left)
                else:
                    return False
            else:
                return False


        return not q1 and not q2 