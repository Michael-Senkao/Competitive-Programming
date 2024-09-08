# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        def countNodes(head):
            count = 0
            curr = head

            while curr is not None:
                count += 1
                curr = curr.next
            return count

        n = countNodes(head)
        full = n // k
        rem = n % k
        ans = []
        curr = head
        
        for _ in range(k):
            dummy = prev = ListNode()
            for _ in range(full):
                prev.next = curr
                prev = prev.next
                curr = curr.next
            if rem > 0:
                rem -= 1
                prev.next = curr
                prev = prev.next
                curr = curr.next

            prev.next = None
            ans.append(dummy.next)

        return ans
        