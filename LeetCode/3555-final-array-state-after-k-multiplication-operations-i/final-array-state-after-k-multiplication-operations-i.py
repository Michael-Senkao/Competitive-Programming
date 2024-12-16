class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        n = len(nums)
        heap = [(val, index) for index,val in enumerate(nums)]
        heapq.heapify(heap)


        while k:
            min_v,index = heapq.heappop(heap)
            min_v *= multiplier
            heapq.heappush(heap, (min_v, index))

            k -= 1
            
        for i in range(n):
            val,index = heap[i]
            nums[index] = val
        return nums