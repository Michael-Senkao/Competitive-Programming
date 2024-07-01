class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def is_prime(num):
            if num <= 1:
                return False
            if num == 2:
                return True
            if num % 2 == 0:
                return False
            for i in range(3, int(num**0.5) +1, 2):
                if num % i == 0:
                    return False
            return True
        
        if left <= 2 and right >= 3:
            return [2, 3] 
        
        if not left & 1:
            left += 1
        a,b = -1, right

        while left <= right:
            x = left + 2
            if is_prime(left):
                while x <= right and not is_prime(x):
                    x += 2
                if x <=right and x - left < b - a:
                    a,b = left,x
                if b-a == 2:
                    return [a,b]
            left = x

        return [-1,-1] if a < 0 else [a,b]