class Solution:
    def compressedString(self, word: str) -> str:
        count = 1
        n = len(word)
        res = []

        for i in range(1, n):
            if count == 9 or word[i] != word[i-1]:
                res.append(str(count))
                res.append(word[i-1])
                count = 0
            count += 1

        res.append(str(count))
        res.append(word[-1])
        return ''.join(res)