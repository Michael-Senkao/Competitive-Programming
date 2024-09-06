# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_set = set(nums)
        dummy = tail = ListNode()
        current_node = head
        while current_node is not None:
            if current_node.val not in nums_set:
                tail.next = current_node
                tail = tail.next
            current_node = current_node.next

        tail.next = None
        return dummy.next
        