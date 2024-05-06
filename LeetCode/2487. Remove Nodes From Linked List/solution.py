# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        ptr = head

        while ptr:
            while stack and ptr.val > stack[-1].val:
                stack.pop()
              
            if stack:
                stack[-1].next = ptr
              
            stack.append(ptr)
            ptr = ptr.next

        head = stack[0]
        return head
