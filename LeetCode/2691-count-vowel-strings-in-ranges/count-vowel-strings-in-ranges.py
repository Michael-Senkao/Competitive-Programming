class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix = []
        count = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        result = []

        for word in words:
            count += (word[0] in vowels and word[-1] in vowels)
            prefix.append(count)

        for l,r in queries:
            start = prefix[l - 1] if l > 0 else 0
            end = prefix[r] 
            result.append(end - start)
        return result
        