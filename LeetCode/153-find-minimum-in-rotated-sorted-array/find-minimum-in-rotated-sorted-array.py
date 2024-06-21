class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = float('inf')
        def binary_search(left, right):
            nonlocal res
            if nums[right] >= nums[left]:
                res = min(res, nums[left])
                return
            mid = (left + right)//2
            res = min(res, nums[mid])
            if nums[mid] >= nums[left]:
                binary_search(mid + 1, right)
            else:
                binary_search(left, mid-1)
        
        binary_search(0, len(nums)-1)
        return res
            