class Solution:
    def mySqrt(self, x: int) -> int:

        def search(num):
            if num*num > x:
                return num - 1
            return search(num + 1)

        return search(1)
        