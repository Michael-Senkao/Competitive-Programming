class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        count = [(value, key) for key,value in count.items()]
        count.sort(reverse=True)
        res = [key for value, key in count[:k]]
        return res