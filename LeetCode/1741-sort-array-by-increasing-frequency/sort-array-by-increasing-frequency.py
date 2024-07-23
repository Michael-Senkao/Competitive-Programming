class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        # print(freq)
        nums.sort(reverse = True)
        nums.sort(key = lambda num: freq[num])
        return nums