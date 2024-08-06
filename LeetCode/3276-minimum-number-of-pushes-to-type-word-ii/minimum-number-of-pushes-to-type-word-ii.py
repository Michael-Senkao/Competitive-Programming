class Solution:
    def minimumPushes(self, word: str) -> int:
        letters = Counter(word)
        sorted_letters = sorted(letters.values())
        result = 0
        i = 1

        while sorted_letters and (i < 4):
            j = 0
            while sorted_letters and j < 8:
                result += (sorted_letters.pop()*i)
                j += 1

            i += 1
        
        while sorted_letters:
            result += sorted_letters.pop()*i
        return result