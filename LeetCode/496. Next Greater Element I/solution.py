class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        next_greater = {}
        stack = []
        ans = []

        # Get the next greater element of each element in 'nums2'
        for i in range(0, n):
            while stack and nums2[i] > stack[-1]:
                next_greater[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(nums2[i])

        # Store the next greater element of each element in 'nums1' in 'ans'
        for num in nums1:
            if num in next_greater:
                ans.append(next_greater[num])
            else:
                ans.append(-1)

        return ans
