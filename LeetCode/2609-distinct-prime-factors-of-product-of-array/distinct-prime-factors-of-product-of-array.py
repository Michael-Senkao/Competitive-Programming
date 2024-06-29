class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def find_prime_factors(n):
            
            if n % 2 == 0:
                distinct_factors.add(2)
    
            # Divide by 2 until n is odd
            while n % 2 == 0:
                n //= 2
        
            # Check for odd factors from 3 to sqrt(n)
            for i in range(3, int(n**0.5) + 1, 2):
                while n % i == 0:
                    distinct_factors.add(i)
                    n //= i
            
            # If n is a prime number greater than 2
            if n > 2:
                distinct_factors.add(n)

        distinct_factors = set()

        for num in nums:
            find_prime_factors(num)

        return len(distinct_factors)