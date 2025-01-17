class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        curr = derived[0]

        for i in range(len(derived)):
            curr = curr ^ derived[i]

        return curr == derived[0]