# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        min_heap = []
        heapq.heapify(min_heap)
        q = deque([root])

        while q:
            curr_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                curr_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if len(min_heap) < k:
                heappush(min_heap, curr_sum)
            elif min_heap[0] < curr_sum:
                heappop(min_heap)
                heappush(min_heap, curr_sum)
        if len(min_heap) < k:
            return -1
        return min_heap[0]
        