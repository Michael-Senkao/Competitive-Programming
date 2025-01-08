class Solution:
    def isPrefixAndSuffix(self, str1, str2):
        return (str2.startswith(str1) and str2.endswith(str1))

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        count = 0

        for i in range(n):
            for j in range(i + 1, n):
                if len(words[i]) <= len(words[j]):
                    count += self.isPrefixAndSuffix(words[i], words[j])
                    

        return count
        