class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        
        word_list = sentence.split()
        n = len(word_list)
        
        if word_list[-1][-1] != word_list[0][0]:
            return False
        for i in range(1, n):
            if word_list[i][0] != word_list[i-1][-1]:
                return False

        return True