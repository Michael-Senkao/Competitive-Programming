class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        def findSubstrings(word):
            m = len(word)

            for i in range(m):
                curr = ''
                for j in range(i, m):
                    curr += word[j]
                    if curr in words_set and len(curr) < m:
                        ans.append(curr)
                        words_set.remove(curr)
        

        n = len(words)
        ans = []
        words_set = set(words)
        for i in range(n):
            if words[i] in words_set:
                findSubstrings(words[i])

        return ans