class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        length = len(flowerbed)
        for i in range(length):
            if flowerbed[i] == 1:
                continue
            if (i - 1 >= 0 and flowerbed[i-1] == 1) or (i + 1 < length and flowerbed[i+1] == 1):
                continue
            flowerbed[i] = 1
            n -= 1
            if n == 0:
                return True
        return False