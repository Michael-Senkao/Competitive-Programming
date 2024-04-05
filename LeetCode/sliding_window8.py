''' 
QUESTION:
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counts = collections.Counter(t) # keep frequency of each character in t
        window = collections.Counter() # keep frequency of each element in a window that are also in t
        start = 0 
        end=0
        n = len(s)
        min_window = "" # holds the minimum substring that satisfies the condition

        # Iterate through s 
        while end < n:
            # if current character is in t, increase its frequency by one
            if s[end] in t:
                window[s[end]] += 1
            
            # Check if current window meets the condition
            while window >= t_counts:
                # Compare lenght of current window and the minimum window so far and take the minimum
                if len(min_window) == 0 or (end - start + 1) < len(min_window):
                    min_window = s[start: end+1]

                # shrink the window until the condition is no longer satisfied 
                if s[start] in t:
                    window[s[start]] -= 1
                
                start += 1
            
            end += 1

        return min_window
        
