from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        sorted_list = SortedList([])
        res = []
        n = len(nums)
        for i in range(n-1, -1, -1):
            index = bisect_left(sorted_list, nums[i])
            res.append(index)
            sorted_list.add(nums[i])

        
        return reversed(res)