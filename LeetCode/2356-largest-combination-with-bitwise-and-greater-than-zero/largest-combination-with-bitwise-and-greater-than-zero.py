class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        
        result = 0
        flag = True

        while flag:
            temp = 0
            flag = False
            for i in range(len(candidates)):
                if not candidates[i]:
                    continue
                temp += candidates[i] & 1
                candidates[i] >>= 1
                flag = True
            result = max(result, temp)
        return result