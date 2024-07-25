class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def heap_sort(nums):
            for i in range(len(nums)):
                heapify_up(i)
            
            for i in range(len(nums) - 1, 0, -1):
                nums[i],nums[0] = nums[0],nums[i]
                heapify_down(0, i - 1)

                
        def heapify_up(index):
            if index > 0:
                parent = (index-1)//2
                if nums[parent] < nums[index]:
                    nums[parent],nums[index] = nums[index],nums[parent]
                    heapify_up(parent)

        def heapify_down(index, n):
            max_index = index
            left = 2*index + 1
            right = left + 1
            if left <= n and nums[left] > nums[max_index]:
                max_index = left
            if right <= n and nums[right] > nums[max_index]:
                max_index = right
            if max_index != index:
                nums[index],nums[max_index] = nums[max_index],nums[index]
                heapify_down(max_index, n)

        
        # print(nums)
        heap_sort(nums)
        return nums