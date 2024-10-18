class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def backtrack(index, bitwise_or):
            if index == len(nums):
                nonlocal ans
                if bitwise_or:
                    count[bitwise_or] += 1
                return
            backtrack(index + 1, bitwise_or | nums[index])
            backtrack(index + 1, bitwise_or)

        count = defaultdict(int)
        ans = 0
        backtrack(0, 0)
        
        return count[max(count.keys())]
            
            
        