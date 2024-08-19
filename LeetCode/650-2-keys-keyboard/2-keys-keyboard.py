class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

        cache = 1
        answer = 1
        onScreen = 1

        while onScreen < n:
            onScreen += cache
            answer += 1 # Pasting
            if onScreen < n and n % onScreen == 0:
                cache = onScreen
                answer += 1 # Copying
        return answer