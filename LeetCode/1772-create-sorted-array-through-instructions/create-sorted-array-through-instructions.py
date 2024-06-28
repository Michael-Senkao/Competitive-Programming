from sortedcontainers import SortedList
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10**9 + 7
        sorted_arr = SortedList()
        res = 0
        for num in instructions:
            res += min(sorted_arr.bisect_left(num), len(sorted_arr) - sorted_arr.bisect_right(num))
            res %= MOD
            sorted_arr.add(num)
        return res
