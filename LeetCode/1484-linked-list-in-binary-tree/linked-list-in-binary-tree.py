# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        @cache
        def helper(treePtr, listPtr):
            if listPtr is None:
                return True
            if treePtr is None:
                return False
    
            if treePtr.val == listPtr.val:
                if listPtr != head and treePtr.val == head.val:
                    return (helper(treePtr.left, listPtr.next) 
                            or helper(treePtr.right, listPtr.next)
                            or helper(treePtr, head))
                else:
                    return (helper(treePtr.left, listPtr.next) 
                            or helper(treePtr.right, listPtr.next))

            if treePtr.val != head.val:
                return (helper(treePtr.left, head) 
                        or helper(treePtr.right, head))
            return (helper(treePtr.left, head.next) 
                    or helper(treePtr.right, head.next))

        return helper(root, head)

        # q = deque([(root, head)])
        # while q:
        #     treePtr, listPtr = q.popLeft()
        