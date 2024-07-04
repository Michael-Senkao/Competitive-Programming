# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead=tail = head.next
        temp = tail.next

        while temp:
            if temp.val == 0:
                tail.next = temp.next
                tail = tail.next
                temp = temp.next
            else:
                tail.val += temp.val
            temp = temp.next if temp else temp
        return newHead