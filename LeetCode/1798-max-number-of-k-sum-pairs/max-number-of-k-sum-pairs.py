class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = 0
        i = 0
        
        # nums.sort()
        found = defaultdict(int)
        while i < n:
            rem = k - nums[i]
            if found[rem] > 0:
                result += 1
                found[rem] -= 1
            else:
                found[nums[i]] += 1
            i += 1

        return result