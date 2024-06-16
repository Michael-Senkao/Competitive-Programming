class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, end):
            if start == end:
                result.append(nums[:])
                return
            for i in range(start, end):
                # Swap the current element with the start element
                nums[start], nums[i] = nums[i], nums[start]
                # Generate all permutations for the next position
                backtrack(start + 1, end)
                # Backtrack (undo the swap)
                nums[start], nums[i] = nums[i], nums[start]

        result = []
        backtrack(0, len(nums))
        return result