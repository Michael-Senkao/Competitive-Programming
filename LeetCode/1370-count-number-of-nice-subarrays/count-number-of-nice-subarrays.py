class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left,right = 0,0
        res = 0
        odd_count = 0

        while right < n:
            if nums[right] & 1: odd_count += 1
            right += 1
            if odd_count == k:
                behind_left = 1
                after_right = 1
                while not nums[left] & 1:
                    behind_left += 1
                    left += 1
                left += 1
                odd_count -= 1
                
                while right < n and not nums[right] & 1:
                    after_right += 1
                    right += 1
                res += behind_left*after_right

        return res