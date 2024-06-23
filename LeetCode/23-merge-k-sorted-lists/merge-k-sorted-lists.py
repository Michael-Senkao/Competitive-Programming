# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        root = None
        heapify(heap)
        
        for x in lists:
            while x:
                heappush(heap, x.val)
                x = x.next
        
        while heap:
            val = heappop(heap)
            if root:
                temp.next = ListNode(val)
                temp = temp.next
            else:
                root = temp = ListNode(val)
        return root