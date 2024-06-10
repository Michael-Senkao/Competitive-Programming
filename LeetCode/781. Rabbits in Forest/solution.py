class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans = 0
        counter = Counter(answers)
        for key in counter:
            sets = counter[key] // (key + 1)
            sets  += counter[key] % (key + 1) != 0
            ans += sets *(key + 1)
            
        return ans
