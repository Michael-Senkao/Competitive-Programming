class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        count = 0
        n = len(arr)
        right = 0
        maxv = float('-inf')
        while right < n:
            maxv= max(maxv,arr[right])
            
            if maxv <= right:
                count+=1
            right+=1
        return count