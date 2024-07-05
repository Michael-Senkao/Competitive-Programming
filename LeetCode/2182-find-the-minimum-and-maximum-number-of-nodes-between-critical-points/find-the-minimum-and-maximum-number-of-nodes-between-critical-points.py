# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        def isCritical(node):
            return left.val < node.val > node.next.val or left.val > node.val < node.next.val
        
        temp = head.next
        left = head
        f,l = -1,-1
        curr = 1
        maxD,minD = -1,float("inf")

        while temp.next:
            if isCritical(temp):
                if f < 0:
                    f,l = curr,curr
                else:
                    maxD = curr - f
                    minD = min(minD, curr - l)
                l = curr
            curr += 1
            left = temp
            temp = temp.next
        
        if maxD <0:
            return [-1, -1]
        return [minD, maxD]