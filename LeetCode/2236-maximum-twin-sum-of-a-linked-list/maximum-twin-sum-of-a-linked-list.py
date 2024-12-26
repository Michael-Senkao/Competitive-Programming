# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = []
        slow = fast = head
        max_twin_sum = 0
        while fast:
            stack.append(slow)
            fast = fast.next.next
            slow = slow.next
        right = stack[-1].next
        while stack:
            left = stack.pop()
            max_twin_sum = max(max_twin_sum, left.val + right.val)
            right = right.next
        return max_twin_sum
        