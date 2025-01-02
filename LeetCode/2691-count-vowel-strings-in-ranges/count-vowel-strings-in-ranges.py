class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n,m = len(words),len(queries)
        prefix = [0]*n
        count = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        result = [0]*m

        for i,word in enumerate(words):
            count += (word[0] in vowels and word[-1] in vowels)
            prefix[i] = count

        for i, (l,r) in enumerate(queries):
            start = prefix[l - 1] if l > 0 else 0
            end = prefix[r] 
            result[i] = end - start
        return result
        