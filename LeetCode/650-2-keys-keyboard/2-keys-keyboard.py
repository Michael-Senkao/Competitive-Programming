class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

        copy = 1
        res = 1
        screen = 1

        while screen < n:
            screen += copy
            res += 1
            if screen < n and n % screen == 0:
                copy = screen
                res += 1
        return res