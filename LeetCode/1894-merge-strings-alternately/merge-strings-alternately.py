class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        result = []
        for k in range(len(word1) + len(word2)):
            if k % 2 == 0 and i < len(word1) or j >= len(word2):
                result.append(word1[i])
                i += 1
            else:
                result.append(word2[j])
                j += 1

        return "".join(result)