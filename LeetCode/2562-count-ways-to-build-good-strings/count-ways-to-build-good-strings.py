class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        @cache
        def backtrack(length):
            if length > high:
                return 0
            
            add_zero = backtrack(length + zero) % MOD
            add_one = backtrack(length + one) % MOD



            return (add_zero + add_one + (low <= length <= high)) % MOD

        MOD = 10**9 + 7
        return backtrack(0)
            
        