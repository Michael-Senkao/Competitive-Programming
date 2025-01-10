class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        freq2 = {}
        res = []

        for word in words2:
            freq = Counter(word)
            for key,val in freq.items():
                freq2[key] = max(freq2.get(key, 0), val)

        for word in words1:
            freq = Counter(word)
            for key,val in freq2.items():
                if freq.get(key, 0) < val:
                    break   
            else:
                res.append(word)
        return res