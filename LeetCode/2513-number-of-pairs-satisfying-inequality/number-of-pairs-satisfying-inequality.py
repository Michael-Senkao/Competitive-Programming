class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        # Sort the array
        def merge_sort(left, right):
            if left < right:
                mid = left +(right - left)//2

                merge_sort(left, mid) # sort left half
                merge_sort(mid + 1, right) # sort right half
                # Count the pairs that satisfies the inequality before merging
                count_pairs(left, mid, right)
                # Merge the two halves
                merge(left, mid, right)
                
            
        # Counts the pairs that satisfies the required inequility
        def count_pairs(left, mid, right):
            i = mid + 1
            while i <= right:
                target = nums[i] + diff
                l,r = left,mid

                while l < r:
                    m = l + (r - l)//2
                    if nums[m] <= target:
                        l = m + 1
                    else:
                        r = m - 1
                
                nonlocal count
                count += l - left
                count = count + 1 if l==r and nums[l]<=target else count
                i += 1
            # print(nums[left:mid+1], nums[mid+1:right+1], count)
        # Merge the two halves of the array created by the merge_sort() function
        def merge(left, mid, right):
            
            temp = []
            i,j = left, mid+1
            while i <= mid and j <= right:
                if nums[j] < nums[i]:
                    temp.append(nums[j])
                    j += 1
                else:
                    temp.append(nums[i])
                    i += 1
            temp.extend(nums[i:mid+1])
            temp.extend(nums[j:right+1])
            nums[left: right+1] = temp[::]


        n = len(nums1)
        count = 0 # To store the pairs that satisfies the inequality

        # Compute 'nums' where nums[i] = nums1[i] - nums2[i]
        nums = [nums1[i]-nums2[i] for i in range(n)]

        # Perform merge sort on 'nums
        merge_sort(0,n - 1)
        
        return count # return result
        