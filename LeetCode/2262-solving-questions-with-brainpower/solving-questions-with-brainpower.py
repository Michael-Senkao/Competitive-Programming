class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        def dp(index):
            if index >= n:
                return 0
            
            if memo[index]:
                return memo[index]
            
            print("solving...")
            solve = questions[index][0] + dp(index + questions[index][1] + 1)
            not_solve = dp(index + 1)

            memo[index] = max(solve, not_solve)
            return memo[index]

        n = len(questions)
        memo = [0 for _ in range(n)]

        dp(0)
        print(memo)
        return max(memo)
