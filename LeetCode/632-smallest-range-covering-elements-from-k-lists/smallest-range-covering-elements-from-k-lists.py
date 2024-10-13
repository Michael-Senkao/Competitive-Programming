class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        n = len(nums)
        start,end = float('-inf'), float("inf")
        
        min_heap = [(nums[i][0], i, 0) for i in range(n)]
        heapify(min_heap)
        max_v = float('-inf')

        for i in range(n):
            max_v = max(max_v, nums[i][0])

        while True:
            min_v, arr, index = heappop(min_heap)
            if end - start > max_v - min_v:
                start,end = min_v,max_v
            index += 1
            if index == len(nums[arr]):
                return [start, end]
            heappush(min_heap, (nums[arr][index], arr, index))
            max_v = max(max_v, nums[arr][index])
        
        return [start, end]
        