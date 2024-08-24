class Solution:
    def reverseWords(self, s: str) -> str:
        str_ = s.strip()
        n = len(str_)
        words = []
    
        i = 0
        while i < n:
            curr = []
            while i < n and str_[i].isalnum():
                curr.append(str_[i])
                i += 1
            while i < n and not str_[i].isalnum():
                i += 1
            words.append("".join(curr))

        l,r = 0,len(words) - 1
        while l < r:
            words[l],words[r] = words[r],words[l]
            l += 1
            r -= 1

        return " ".join(words)
