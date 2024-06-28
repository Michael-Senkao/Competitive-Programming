from sortedcontainers import SortedList
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10**9 + 7
        # n = len(instructions)
        sorted_arr = SortedList()
        # sorted_arr.add(instructions[0])
        res = 0
        for num in instructions:
            # if instructions[i] == sorted_arr[0] or instructions[i] == sorted_arr[0]:
            #     sorted_arr.add(instructions[i])
            #     continue
            res += min(sorted_arr.bisect_left(num), len(sorted_arr) - sorted_arr.bisect_right(num))
            res %= MOD
            sorted_arr.add(num)
        return res