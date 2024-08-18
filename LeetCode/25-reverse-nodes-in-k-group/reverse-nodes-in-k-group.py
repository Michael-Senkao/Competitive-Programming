# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(prev, curr):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            return (curr,prev)

        dummy = tail = ListNode()

        curr_head = head
        while curr_head:
            prev, curr = None,curr_head
        
            for _ in range(k):
                if not curr:
                    while prev:
                        prev,curr = reverse(curr, prev)

                    tail.next = curr
                    curr_head = None
                    break
                
                curr,prev = reverse(prev, curr)
            else:
                tail.next = prev
                tail = curr_head
                curr_head = curr
        
        return dummy.next
        