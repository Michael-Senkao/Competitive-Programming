class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        freq1 = {}
        freq2 = {}
        values_freq1 = {}
        values_freq2 = {}

        for i in range(len(word1)):
            freq1[word1[i]] = freq1.get(word1[i], 0) + 1
            freq2[word2[i]] = freq2.get(word2[i], 0) + 1

        for key,value in freq1.items():
            if key not in freq2:
                return False
            values_freq1[value] = values_freq1.get(value, 0) + 1

        for key,value in freq2.items():
            if key not in freq2 or value not in values_freq1:
                return False
            values_freq2[value] = values_freq2.get(value, 0) + 1

        for value, count in values_freq1.items():
            if values_freq2[value] != count:
                return False
        return True
