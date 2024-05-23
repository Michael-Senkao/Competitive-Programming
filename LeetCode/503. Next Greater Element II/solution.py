class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1]*n
        stack = []

        for i in range(2*n):
            index = i % n
            while stack and nums[index] > nums[stack[-1]]:
                ans[stack[-1]] = nums[index]
                stack.pop()
            stack.append(index)
            i += 1

        return ans

        
