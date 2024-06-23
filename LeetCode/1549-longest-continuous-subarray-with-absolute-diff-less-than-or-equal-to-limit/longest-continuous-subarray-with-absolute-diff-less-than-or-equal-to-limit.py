class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        maximum,minimum = [],[]
        heapify(maximum)
        heapify(minimum)

        left, right = 0,0
        res = 0
        while right < n:
            heappush(maximum,(-1*nums[right], right))
            heappush(minimum,(nums[right], right))

            while -1*maximum[0][0] - minimum[0][0] > limit:
                left += 1
                while minimum[0][1] < left:
                    heappop(minimum)
                while maximum[0][1] < left:
                    heappop(maximum)
            
            res = max(res, right - left + 1)
            right += 1
        return res
