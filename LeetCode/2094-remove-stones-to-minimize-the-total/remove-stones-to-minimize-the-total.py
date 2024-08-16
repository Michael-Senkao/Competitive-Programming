import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        total_stones = 0

        for pile in piles:
            heapq.heappush(heap, -pile)

        while heap and k > 0:
            largest = -heapq.heappop(heap)
            second_largest = -heap[0] if heap else 0
            while k > 0 and largest >= second_largest:
                largest -= largest//2
                k -= 1
                if largest == 0:
                    break
            if largest > 0:
                heapq.heappush(heap,-largest)
            


        return -sum(heap)