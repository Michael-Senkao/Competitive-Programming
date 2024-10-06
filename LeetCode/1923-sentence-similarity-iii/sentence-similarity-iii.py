class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        
        sentence1 = sentence1.split()
        sentence2 = sentence2.split()
    
        count = 0
        
        if len(sentence1) < len(sentence2):
            sentence2,sentence1 = sentence1,sentence2

        n1,n2 = len(sentence1), len(sentence2)
        i = j = 0
        while i < len(sentence1) and j < len(sentence2) and sentence1[i] == sentence2[j]:
            i += 1
            j += 1
            count += 1

        if count == n2:
            return True

        stop = j - 1
        i = n1 - 1
        j = n2 - 1
        while i >= 0 and j > stop and sentence1[i] == sentence2[j]:
            i -= 1
            j -= 1
            count += 1
        
        return count == n2
        
            

        return i == len(sentence1) and j == len(sentence2) if sub else True