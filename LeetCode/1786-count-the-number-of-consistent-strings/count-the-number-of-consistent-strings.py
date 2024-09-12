class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        ans = 0
        for word in words:
            word_set = set(word)
            for letter in word_set:
                if letter not in allowed_set:
                    break
            else:
                ans += 1

        return ans