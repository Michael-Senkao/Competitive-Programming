class Solution:
    def getPairsCount(self, arr, n, k):
       
        freq = {}
        res = 0
        
        for num in arr:
            diff = k - num
            if diff in freq:
                res += freq[diff]
            freq[num] = freq[num] + 1 if num in freq else 1
        
        return res
