class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i = 0
        s = ""

        while i < n:
            char = chars[i]
            count = 1
            i += 1
            while i < n and chars[i] == chars[i-1]:
                count += 1
                i += 1
            s += char
            if count > 1:
                s += str(count)
        for i in range(len(s)):
            if i < n:
                chars[i] = s[i]
            else:
                chars.append(s[i])
        return len(s)


        