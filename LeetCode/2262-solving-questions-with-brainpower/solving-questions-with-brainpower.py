class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        # Top Down DP
        # def dp(index):
        #     if index >= n:
        #         return 0
            
        #     if memo[index]:
        #         return memo[index]
            
        #     solve = questions[index][0] + dp(index + questions[index][1] + 1)
        #     not_solve = dp(index + 1)

        #     memo[index] = max(solve, not_solve)
        #     return memo[index]

        n = len(questions)
        dp = [0 for _ in range(n)]

        # Bottom-Up DP
        for i in range(n-1,-1,-1):
            nextIndex = i + questions[i][1] + 1
            pick = dp[nextIndex] + questions[i][0] if nextIndex < n else questions[i][0]
            notpick = dp[i+1] if i+1 < n else 0
            dp[i] = max(pick,notpick)
        return dp[0]
