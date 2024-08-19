class Solution:
    def minSteps(self, n: int) -> int:
        def is_prime(n):
            if n <= 1:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            for i in range(3, int(n**0.5) + 1, 2):
                if n % i == 0:
                    return False
            return True

        if n == 1:
            return 0
        if is_prime(n):
            return n

        cache = 1
        answer = 1
        onScreen = 1

        while onScreen < n:
            onScreen += cache # Pasting
            answer += 1 # Cost of Pasting
            if onScreen < n and n % onScreen == 0:
                cache = onScreen # Copying
                answer += 1 # Cost of Copying
        return answer