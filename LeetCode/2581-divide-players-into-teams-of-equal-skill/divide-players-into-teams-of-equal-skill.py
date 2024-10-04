class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        if n == 2:
            return skill[0]*skill[1]
            
        result = 0
        size = sum(skill)*2 // n
        found = defaultdict(int)

        for num in skill:
            need = size - num
            if need in found:
                result += need*num
                found[need] -= 1
                if found[need] == 0:
                    del found[need]
            else:
                found[num] += 1

        return result if len(found) == 0 else -1