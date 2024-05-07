# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Extract the number from the linked list
        num = 0
        while head:
            num = num*10 + head.val
            head = head.next

        if num == 0:
            return ListNode(0)
            
        # Double the number
        num *= 2

        # Reconstruct the linked list with the doubled number
        while num > 0:
            head = ListNode(num % 10, head)
            num //= 10

        # Return head of new linked list
        return head
