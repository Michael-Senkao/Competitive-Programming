import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        total_stones = 0

        for pile in piles:
            heapq.heappush(heap, -pile)

        while heap and k > 0:
            largest = -heapq.heappop(heap)
            largest -= largest//2
            heapq.heappush(heap,-largest)
            k -= 1


        return -sum(heap)