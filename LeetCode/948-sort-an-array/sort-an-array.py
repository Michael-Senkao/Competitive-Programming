class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(left, right, arr):
            if left < right:
                mid = (left + right)//2
                return merge(mergeSort(left, mid, arr), mergeSort(mid + 1, right, arr))
            return [arr[left]]
        
        def merge(left, right):
            n,m = len(left),len(right)
            i,j = 0,0
            res = []
            while i < n and j < m:
                if right[j] < left[i]:
                    res.append(right[j])
                    j += 1
                else:
                    res.append(left[i])
                    i += 1
            
            res.extend(left[i:])
            res.extend(right[j:])
            return res

        return mergeSort(0, len(nums)-1, nums)