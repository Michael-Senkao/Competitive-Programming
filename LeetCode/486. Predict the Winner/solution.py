class Solution:
    def max_value(self, nums, left, right):
        if left == right:
            return nums[left]
        return max(nums[left] + self.min_value(nums, left+1, right), nums[right] + self.min_value(nums, left, right-1))
        
    def min_value(self, nums, left, right):
        if left == right:
            return 0
        return min(self.max_value(nums, left+1, right), self.max_value(nums, left, right-1))
   
            

       
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        total = self.max_value(nums, 0, len(nums) -1)
        return total >= sum(nums) - total
