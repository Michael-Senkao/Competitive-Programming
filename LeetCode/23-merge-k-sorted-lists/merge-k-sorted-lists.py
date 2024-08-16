# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeSort(left, right):
            if left < right:
                mid = left + (right - left)//2
                l = mergeSort(left, mid)
                r = mergeSort(mid+1, right)
                return merge(l, r)

            return lists[left]
        
        def merge(left, right):
            dummy = curr = ListNode()
            while left and right:
                if left.val < right.val:
                    curr.next = left
                    left = left.next
                else:
                    curr.next = right
                    right = right.next
                curr = curr.next
            if left:
                curr.next = left
            if right:
                curr.next = right
            # print_(dummy.next)
            return dummy.next
        # def print_(start):
        #     while start:
        #         print(start.val, end="->")
        #         start = start.next
        #     print()
        if not lists: return None
        return mergeSort(0, len(lists) - 1)
        