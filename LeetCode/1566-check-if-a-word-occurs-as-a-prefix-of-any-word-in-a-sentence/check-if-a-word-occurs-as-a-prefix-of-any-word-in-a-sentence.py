class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
    
        for index in range(len(words)):
            word = words[index]
            i,j = 0,0
            while i < len(word) and j < len(searchWord) and word[i]==searchWord[j]:
                i += 1
                j += 1
            if j == len(searchWord):
                return index + 1
        return -1