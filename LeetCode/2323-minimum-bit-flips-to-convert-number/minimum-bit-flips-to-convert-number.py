class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        max_ = max(start, goal)
        ans = 0
        
        while start > 0 or goal > 0:
            start_bit = start & 1
            end_bit = goal & 1
            ans += start_bit!=end_bit
            start >>= 1
            goal >>= 1
       
        return ans
        