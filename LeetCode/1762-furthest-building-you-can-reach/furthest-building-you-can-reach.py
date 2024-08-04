class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        max_heap = []
        heapify(max_heap)
        i = 0

        while i < n - 1:
            diff = heights[i + 1] - heights[i]
            heappush(max_heap, -diff)
            if diff > 0:
                if bricks >= diff:
                    bricks -= diff
                elif ladders > 0:
                    ladders -= 1
                    max_brick = -heappop(max_heap)
                    bricks += max_brick - diff
                else:
                    return i
            i += 1
        return i