'''
QUESTION:
Given a string s, find the length of the longest substring without repeating characters.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        window = Counter()
        left, right, ans = [0]*3

        # Iterate over s with a dynamic window
        while right < n:
            # Increase the count of current character
            window[s[right]] += 1

            # Shrink the window until no character appears more than once
            while window[s[right]] > 1:
                window[s[left]] -= 1
                left += 1
            
            # Choose longest window (substring) so far
            ans = max(ans, right - left + 1)
            right += 1 
    
        return ans
