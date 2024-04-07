'''
Question:
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the
original letters exactly once.
'''
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        n = len(s)
        k = len(p)
        answer = []

        target = collections.Counter(p) # Count the occurences of each character in p
        window = collections.Counter(s[:k]) # Count the occurences of each character in the window

        # Check if current window is an anagram of p, if so add the start index
        if window == target:
            answer.append(0)

        # Iterate through s with a window of size k
        for index in range(k, n):
            # Increment the count of current character
            window[s[index]] += 1

            # Shrink the window while decrementing the count of the last character
            if window[s[index-k]] == 1:
                window.pop(s[index - k])
            else:
                window[s[index - k]] -= 1
            
            # Check if current window is an anagram of p, if so add the start index
            if window == target:
                answer.append(index - k + 1)
        
        return answer
        
