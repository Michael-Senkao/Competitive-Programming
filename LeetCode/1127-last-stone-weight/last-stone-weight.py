class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapify(heap)
        while len(heap) > 1:
            y,x = -heappop(heap),-heappop(heap)
            if x!=y:
                heappush(heap, -(y-x))
        return -heap[0] if heap else 0
