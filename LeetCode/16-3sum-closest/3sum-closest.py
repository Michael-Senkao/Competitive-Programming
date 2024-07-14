class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        res = sum(nums[:3])

        for i in range(n):
            l,r = i+1, n-1
            diff = abs(target - res)
            while l < r:
                _sum = nums[l] + nums[r] + nums[i]
                if abs(target - _sum) < diff:
                    res = _sum
                if _sum > target:
                    r -= 1
                elif _sum < target:
                    l += 1
                else:
                    return target

        return res