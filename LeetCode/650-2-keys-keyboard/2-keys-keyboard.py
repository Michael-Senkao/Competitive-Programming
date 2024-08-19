class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

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