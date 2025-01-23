# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for index, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, index))


        dummy = tail = ListNode()
        while min_heap:
            val,index = heapq.heappop(min_heap)
            tail.next = ListNode(val)
            tail = tail.next

            lists[index] = lists[index].next
            if lists[index]:
                heapq.heappush(min_heap, (lists[index].val, index))

        return dummy.next