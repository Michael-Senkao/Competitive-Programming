class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sum_of_chalks = sum(chalk)
        passes = k // sum_of_chalks
        remainder = k - passes*sum_of_chalks
        index = 0

        while remainder >= chalk[index]:
            remainder -= chalk[index]
            index += 1
        return index
