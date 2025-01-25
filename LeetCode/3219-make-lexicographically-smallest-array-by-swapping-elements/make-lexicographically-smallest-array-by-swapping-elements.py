class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        sorted_nums = [(index,val) for val,index in enumerate(nums)]
        sorted_nums.sort()
        
        mappings = {}
        mappings[sorted_nums[0][1]] = 0

        buckets = [[0,0]] # (start_index, end_index)`
        
        for i in range(1,n):
            if sorted_nums[i][0] - sorted_nums[i-1][0] > limit:
                buckets.append([i,i]) # Create new bucket initialized with curr_index
            else:
                buckets[-1][1]=i # Update end_index of current bucket
            
            current_index = sorted_nums[i][1]
            mappings[current_index] = len(buckets)-1

        for i in range(n):
            bucket_index = mappings[i]
            val_index = buckets[bucket_index][0]
            nums[i] = sorted_nums[val_index][0]
            buckets[bucket_index][0]+=1   

        return nums