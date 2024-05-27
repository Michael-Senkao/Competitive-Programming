class Solution:
    def power(self, a, b):
        MOD = 10**9 + 7
        result = 1
        while b > 0:
            if b % 2 == 1:
                result = (result * a) % MOD
            a = (a * a) % MOD
            b //= 2
        return result

    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        even_power = odd_power = n//2
        even_power += n%2 == 1

        even_product = self.power(5, even_power)
        odd_product = self.power(4, odd_power)
        
        return (even_product*odd_product)%MOD
        
