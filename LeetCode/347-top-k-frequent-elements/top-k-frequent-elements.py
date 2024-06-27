class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        count = [(-value, key) for key,value in count.items()]
        res = []
        heapify(count)
        for i in range(k):
            res.append(heappop(count)[1])
        return res