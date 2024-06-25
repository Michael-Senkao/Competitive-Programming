class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(left, right):
            if left < right:
                mid = left + (right - left)//2

                merge_sort(left, mid)
                merge_sort(mid+1, right)
                count_pairs(left, mid, right) 
                merge(left, mid, right)
                       

        def merge(left, mid, right):
            i,j = left,mid+1
            temp = []
            while i <= mid and j <= right:
                if nums[i] < nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
                
            temp.extend(nums[i:mid + 1])
            temp.extend(nums[j: right + 1])
            nums[left: right + 1] = temp[::]

        def count_pairs(left, mid, right):
            i,j = left,mid+1
            while i <= mid and j <= right:
                if nums[i] > 2*nums[j]:
                    count[0] += mid - i + 1
                    j += 1
                else:
                    i += 1

        count = [0]
        merge_sort(0, len(nums) - 1)

        return count[0]