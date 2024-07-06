class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        passes = time //(n-1)
        remainder = time % (n-1)

        return n - remainder if passes & 1 else remainder + 1 