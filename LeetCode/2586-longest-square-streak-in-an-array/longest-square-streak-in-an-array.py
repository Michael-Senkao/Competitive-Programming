class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums_set = set(nums)
        set_keys = {num:num for num in nums_set}
        square_streak = {num: set([num]) for num in nums_set}
        
        for num in nums_set:
            square_root = math.sqrt(num)
            if square_root*square_root == num and square_root in nums_set:
                set_key = set_keys[num]
                square_streak[set_keys[square_root]] = square_streak[set_keys[square_root]] | square_streak[set_key]
                
                for x in square_streak[set_key]:
                    set_keys[x] = set_keys[square_root]
                del square_streak[set_key]

        # print(square_streak)
        # print(set_keys)
        result = 0
        for key,value in square_streak.items():
            result = max(result, len(value))
        return result if result > 1 else -1
        