class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        toExchange = numBottles
        while toExchange//numExchange > 0:
            res += toExchange//numExchange
            toExchange = toExchange//numExchange + toExchange%numExchange
        
        return res