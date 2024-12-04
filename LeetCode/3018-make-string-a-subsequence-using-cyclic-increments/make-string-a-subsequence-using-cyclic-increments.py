class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        n1 = len(str1)
        n2 = len(str2)

        if n1 < n2:
            return False

        i, j = 0, 0
        while i < n1 and j < n2:
            pos1, pos2  = ord(str1[i]) - 97, ord(str2[j]) - 97
            if pos1 == pos2 or (pos1 + 1) % 26 == pos2:
                j += 1

            i += 1


        return j == n2
        