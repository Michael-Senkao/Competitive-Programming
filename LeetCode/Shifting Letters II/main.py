class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        char_shifts = [0]*n
        ans = []

        for shift in shifts:
            if shift[2]:
                char_shifts[shift[0]] += 1
                if shift[1]+1<n:
                    char_shifts[shift[1] + 1] -= 1
            else:
                char_shifts[shift[0]] -= 1
                if shift[1]+1<n:
                    char_shifts[shift[1] + 1] += 1
            

        for i in range(1,n):
            char_shifts[i] += char_shifts[i-1]
        
        for i in range(n):
            ans.append(chr(((ord(s[i]) - ord('a') + char_shifts[i])%26) + ord('a')))
        return "".join(ans)
