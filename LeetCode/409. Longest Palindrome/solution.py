class Solution:
    def longestPalindrome(self, s: str) -> int:
        ''' 1:
        letter_counts = Counter(s)
        res = 0

        for count in letter_counts.values():
            res += count // 2
        
        res *= 2
        if res < len(s):
            res += 1
        '''
        
        count = set()
        res = 0

        for letter in s:
            if letter in count:
                count.discard(letter)
                res += 2
            else:
                count.add(letter)
                
        return res + 1 if count else res
