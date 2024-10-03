class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        total_sum = sum(nums)
        remainder = total_sum % p
        ans = n
        if remainder == 0:
            return 0

        prefix_sum = defaultdict(int)
        prefix_sum[0] = -1
        current_sum = 0
        for i in range(n):
            current_sum += nums[i]
            key = current_sum%p - remainder
            if key < 0:
                key += p
            if key in prefix_sum:
                ans = min(ans, i - prefix_sum[key])
            
            prefix_sum[current_sum%p] = i

        ans = -1 if ans == n else ans
        return ans