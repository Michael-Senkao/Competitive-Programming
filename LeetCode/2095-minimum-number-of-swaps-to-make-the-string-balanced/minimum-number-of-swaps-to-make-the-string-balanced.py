class Solution:
    def minSwaps(self, s: str) -> int:
        left,right = 0, len(s) - 1
        open = close = result = 0

        while left < right:
            if s[left] == '[':
                open += 1
            elif open > 0:
                open -= 1
            else:
                result += 1
                open += 1
                while s[right] == ']':
                    right -= 1
                right -= 1
            left += 1

        return result


        