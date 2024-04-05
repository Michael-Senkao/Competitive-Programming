''' 
QUESTION:
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s1) > len(s2)):
            return False
        
        s1_counts = collections.Counter(s1)
        window = collections.Counter()
        k = len(s1)
        n = len(s2)
        end = 0

        # Get the first k characters in s2 into the window
        while end < k:
            window[s2[end]] += 1
            end += 1
        if window == s1_counts:
            return True
        
        if window[s2[0]] == 1:
            del window[s2[0]]
        else:
            window[s2[0]] -= 1

        # Slide the window over the remaining n - k elements to find a window that satisfies the condition
        while end < n:
            window[s2[end]] += 1
            if window == s1_counts:
                return True
            
            if window[s2[end - k +1]] == 1:
                del window[s2[end - k + 1]]
            else:
                window[s2[end - k + 1]] -= 1

            end += 1
            
        return False
