class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        heapify(heap)
        total_stones = 0

        for pile in piles:
            total_stones += pile
            heappush(heap, -pile)

        while k > 0:
            curr = -heappop(heap)
            if curr == 0:
                return 0
            total_stones -= int(curr/2)
            curr -= int(curr/2)
            heappush(heap, -curr)

            k -= 1
        return total_stones
        