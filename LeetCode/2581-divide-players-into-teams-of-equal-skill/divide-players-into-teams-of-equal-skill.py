class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        if n == 2:
            return skill[0]*skill[1]

            
        skill.sort()
        result = 0
        size = skill[0] + skill[-1]
        left,right = 0, n - 1

        while left < right:
            if skill[left] + skill[right] != size:
                return -1
            result += skill[left]*skill[right]
            left += 1
            right -= 1

        return result