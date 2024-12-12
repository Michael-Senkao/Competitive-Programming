class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap = [-gift for gift in gifts]
        heapq.heapify(max_heap)

        while k and max_heap[0] != -1:
            largest_gift = -heapq.heappop(max_heap)
            heapq.heappush(max_heap, -int(math.sqrt(largest_gift)))
            k -= 1

        return -sum(max_heap)