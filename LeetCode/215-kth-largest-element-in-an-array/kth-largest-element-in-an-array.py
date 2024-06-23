class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapify(heap)
        for num in nums:
            heappush(heap, -num)
        
        for _ in range(1, k):
            heappop(heap)
        
        return -heappop(heap)