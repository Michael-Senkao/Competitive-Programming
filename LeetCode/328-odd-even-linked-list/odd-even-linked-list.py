# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        i = 1
        curr = head.next.next
        odd_head = odd_tail = head
        even_head = even_tail = head.next
        even_tail.next = odd_tail.next = None
        
        while curr:
            if i & 1:
                odd_tail.next = curr
                odd_tail = curr
            else:
                even_tail.next = curr
                even_tail = curr
            i += 1
            curr = curr.next

        even_tail.next = None
        odd_tail.next = even_head
        return odd_head