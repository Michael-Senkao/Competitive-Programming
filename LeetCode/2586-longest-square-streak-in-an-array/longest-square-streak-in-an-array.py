class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums_set = set(nums)
        found = defaultdict(int)
        result = 0
        for num in nums:
            curr = num
            count = 1
            square = curr * curr
            while square in nums_set:
                if square in found:
                    count += found[square]
                    break
                count += 1
                square *= square
            result = max(result, count)
            found[num] = count


        
        return result if result > 1 else -1
        