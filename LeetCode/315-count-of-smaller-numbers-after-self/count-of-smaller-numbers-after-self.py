class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def mergeSort(l, r):
            if l < r:
                mid = l + (r - l)//2
                left = mergeSort(l, mid)
                right = mergeSort(mid + 1, r)
                return merge(left, right)
            
            return [arr[l]]

            
        def merge(left, right):
            i = j = 0
            count = 0
            merged_arr = []
    
            while i < len(left) and j < len(right):
                
                if left[i][1] <= right[j][1]:
                    counts[left[i][0]] += count
                    merged_arr.append(left[i])
                    i += 1
                else:
                    count += 1
                    merged_arr.append(right[j])
                    j += 1

            while i < len(left):
                counts[left[i][0]] += count
                merged_arr.append(left[i])
                i += 1
            while j < len(right):
                merged_arr.append(right[j])
                j += 1
            return merged_arr

        n = len(nums)
        arr = [(index, num) for index,num in enumerate(nums)]
        counts = [0 for _ in range(n)]

        mergeSort(0, n-1)

        return counts
        