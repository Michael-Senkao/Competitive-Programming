class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_dict = Counter(s1.split())
        s2_dict = Counter(s2.split())
        ans = []
        
        for word,count in s1_dict.items():
            if count + s2_dict[word] == 1:
                ans.append(word)
        for word,count in s2_dict.items():
            if count + s1_dict[word] == 1:
                ans.append(word)

        return ans