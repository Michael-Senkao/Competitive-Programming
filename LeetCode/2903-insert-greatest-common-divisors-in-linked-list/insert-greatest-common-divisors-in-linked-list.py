# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def find_gcd(a,b):
            if b == 0:
                return a
            return find_gcd(b, a%b)

        curr = head
        while curr.next:
            gcd = ListNode(find_gcd(curr.val, curr.next.val), curr.next)
            curr.next = gcd
            curr = gcd.next
        return head
        