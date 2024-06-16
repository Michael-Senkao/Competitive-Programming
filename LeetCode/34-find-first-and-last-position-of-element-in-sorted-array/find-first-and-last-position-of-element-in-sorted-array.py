class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        n = len(nums)

        if not n:
            return res

           
        left,right = 0,n-1
        # Find first occurance of target if it exists
        while left < right:
            mid = (left + right)//2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1

        if nums[left] != target:
            return res # Target not in nums

        # Find last occurance of target in nums
        res[0] = left
        right = n -1
        while left < right:
            mid = math.ceil((left + right)/2)
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        
        res[1] = right

        return res