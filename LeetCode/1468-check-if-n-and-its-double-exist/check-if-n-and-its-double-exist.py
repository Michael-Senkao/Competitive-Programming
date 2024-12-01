class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        found = set()

        for num in arr:
            if 2*num in found:
                return True
            if num % 2 == 0 and num//2 in found:
                return True
            found.add(num)

        return False