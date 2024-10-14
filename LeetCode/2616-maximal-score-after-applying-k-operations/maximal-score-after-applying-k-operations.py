class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)

        result = 0

        for _ in range(k):
            max_v = -heapq.heappop(max_heap)
            result += max_v
            heapq.heappush(max_heap, -math.ceil(max_v / 3))

        return result